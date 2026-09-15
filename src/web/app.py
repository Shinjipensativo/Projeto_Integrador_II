from datetime import datetime
import os
from pathlib import Path
import sqlite3

from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for


BASE_DIR = Path(__file__).resolve().parent
DATABASE = Path(os.environ.get("ACESSOLAB_DATABASE", BASE_DIR / "acessolab.db"))

app = Flask(__name__)
app.config["SECRET_KEY"] = "acessolab-demonstracao"

LABORATORIOS = (
    "Laboratório de Robótica",
    "Laboratório de Informática 1",
    "Laboratório de Informática 2",
)


def conectar():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_banco():
    with conectar() as conexao:
        conexao.executescript(
            """
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula TEXT NOT NULL UNIQUE,
                nome TEXT NOT NULL,
                turma TEXT NOT NULL,
                ativo INTEGER NOT NULL DEFAULT 1
            );

            CREATE TABLE IF NOT EXISTS acessos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER,
                matricula_informada TEXT NOT NULL,
                data_hora TEXT NOT NULL,
                tipo TEXT,
                laboratorio TEXT,
                resultado TEXT NOT NULL,
                FOREIGN KEY (aluno_id) REFERENCES alunos(id)
            );
            """
        )

        # Atualiza bancos criados por versões anteriores sem apagar os dados.
        colunas = {
            coluna["name"]
            for coluna in conexao.execute("PRAGMA table_info(acessos)").fetchall()
        }
        if "laboratorio" not in colunas:
            conexao.execute("ALTER TABLE acessos ADD COLUMN laboratorio TEXT")


def registrar_acesso(matricula, laboratorio):
    matricula = str(matricula).strip()
    laboratorio = str(laboratorio).strip()

    if laboratorio not in LABORATORIOS:
        return {
            "autorizado": False,
            "mensagem": "Selecione um laboratório válido.",
            "matricula": matricula,
        }

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with conectar() as conexao:
        aluno = conexao.execute(
            "SELECT * FROM alunos WHERE matricula = ?", (matricula,)
        ).fetchone()

        if aluno is None or not aluno["ativo"]:
            conexao.execute(
                """
                INSERT INTO acessos
                    (aluno_id, matricula_informada, data_hora, tipo, laboratorio, resultado)
                VALUES (NULL, ?, ?, NULL, ?, 'Negado')
                """,
                (matricula, agora, laboratorio),
            )
            return {
                "autorizado": False,
                "mensagem": "Matrícula não cadastrada ou inativa.",
                "matricula": matricula,
                "laboratorio": laboratorio,
                "tipo": None,
            }

        ultimo = conexao.execute(
            """
            SELECT tipo FROM acessos
            WHERE aluno_id = ? AND laboratorio = ? AND resultado = 'Autorizado'
            ORDER BY id DESC LIMIT 1
            """,
            (aluno["id"], laboratorio),
        ).fetchone()

        tipo = "Saída" if ultimo and ultimo["tipo"] == "Entrada" else "Entrada"
        conexao.execute(
            """
            INSERT INTO acessos
                (aluno_id, matricula_informada, data_hora, tipo, laboratorio, resultado)
            VALUES (?, ?, ?, ?, ?, 'Autorizado')
            """,
            (aluno["id"], matricula, agora, tipo, laboratorio),
        )

        return {
            "autorizado": True,
            "mensagem": f"{tipo} registrada para {aluno['nome']}.",
            "nome": aluno["nome"],
            "matricula": matricula,
            "tipo": tipo,
            "laboratorio": laboratorio,
            "data_hora": agora,
        }


@app.route("/")
def inicio():
    with conectar() as conexao:
        total_alunos = conexao.execute(
            "SELECT COUNT(*) FROM alunos WHERE ativo = 1"
        ).fetchone()[0]
        total_acessos = conexao.execute(
            "SELECT COUNT(*) FROM acessos WHERE resultado = 'Autorizado'"
        ).fetchone()[0]
        presentes = conexao.execute(
            """
            SELECT a.nome, a.matricula, a.turma, x.laboratorio
            FROM alunos a
            JOIN acessos x ON x.id = (
                SELECT x2.id FROM acessos x2
                WHERE x2.aluno_id = a.id
                  AND x2.resultado = 'Autorizado'
                ORDER BY x2.id DESC LIMIT 1
            )
            WHERE a.ativo = 1 AND x.tipo = 'Entrada'
            ORDER BY a.nome
            """
        ).fetchall()
        recentes = conexao.execute(
            """
            SELECT x.*, a.nome
            FROM acessos x
            LEFT JOIN alunos a ON a.id = x.aluno_id
            ORDER BY x.id DESC LIMIT 8
            """
        ).fetchall()

    return render_template(
        "inicio.html",
        total_alunos=total_alunos,
        total_acessos=total_acessos,
        presentes=presentes,
        recentes=recentes,
        laboratorios=LABORATORIOS,
        simulacao=session.pop("ultima_simulacao", None),
    )


@app.route("/registrar", methods=["POST"])
def registrar():
    resultado = registrar_acesso(
        request.form.get("matricula", ""),
        request.form.get("laboratorio", ""),
    )
    session["ultima_simulacao"] = resultado
    flash(resultado["mensagem"], "sucesso" if resultado["autorizado"] else "erro")
    return redirect(url_for("inicio"))


@app.route("/alunos", methods=["GET", "POST"])
def alunos():
    if request.method == "POST":
        matricula = request.form.get("matricula", "").strip()
        nome = request.form.get("nome", "").strip()
        turma = request.form.get("turma", "").strip()

        if not matricula or not nome or not turma:
            flash("Preencha todos os campos.", "erro")
        else:
            try:
                with conectar() as conexao:
                    conexao.execute(
                        "INSERT INTO alunos (matricula, nome, turma) VALUES (?, ?, ?)",
                        (matricula, nome, turma),
                    )
                flash("Aluno cadastrado com sucesso.", "sucesso")
            except sqlite3.IntegrityError:
                flash("Essa matrícula já está cadastrada.", "erro")
        return redirect(url_for("alunos"))

    with conectar() as conexao:
        lista = conexao.execute("SELECT * FROM alunos ORDER BY nome").fetchall()
    return render_template("alunos.html", alunos=lista)


@app.post("/alunos/<int:aluno_id>/status")
def alterar_status(aluno_id):
    with conectar() as conexao:
        conexao.execute(
            "UPDATE alunos SET ativo = CASE ativo WHEN 1 THEN 0 ELSE 1 END WHERE id = ?",
            (aluno_id,),
        )
    flash("Situação do aluno atualizada.", "sucesso")
    return redirect(url_for("alunos"))


@app.route("/historico")
def historico():
    busca = request.args.get("busca", "").strip()
    with conectar() as conexao:
        registros = conexao.execute(
            """
            SELECT x.*, a.nome, a.turma
            FROM acessos x
            LEFT JOIN alunos a ON a.id = x.aluno_id
            WHERE ? = ''
               OR x.matricula_informada LIKE ?
               OR COALESCE(a.nome, '') LIKE ?
               OR COALESCE(x.laboratorio, '') LIKE ?
            ORDER BY x.id DESC
            """,
            (busca, f"%{busca}%", f"%{busca}%", f"%{busca}%"),
        ).fetchall()
    return render_template("historico.html", registros=registros, busca=busca)


@app.post("/api/acesso")
def api_acesso():
    dados = request.get_json(silent=True) or {}
    matricula = dados.get("matricula", "")
    laboratorio = dados.get("laboratorio", LABORATORIOS[0])
    if not str(matricula).strip():
        return jsonify({"autorizado": False, "mensagem": "Informe a matrícula."}), 400

    resultado = registrar_acesso(matricula, laboratorio)
    return jsonify(resultado), 200 if resultado["autorizado"] else 403


criar_banco()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
