import os
from pathlib import Path
import sys
import tempfile
import unittest


WEB_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WEB_DIR))

TEMP_DIR = tempfile.TemporaryDirectory()
os.environ["ACESSOLAB_DATABASE"] = str(Path(TEMP_DIR.name) / "teste.db")

import app as acessolab


class AcessoLabTestes(unittest.TestCase):
    def setUp(self):
        acessolab.app.config.update(TESTING=True)
        self.client = acessolab.app.test_client()
        with acessolab.conectar() as conexao:
            conexao.execute("DELETE FROM acessos")
            conexao.execute("DELETE FROM alunos")
            conexao.execute(
                "INSERT INTO alunos (matricula, nome, turma) VALUES (?, ?, ?)",
                ("2026001", "Aluno Teste", "3º B"),
            )

    def test_painel_exibe_laboratorios(self):
        resposta = self.client.get("/")
        pagina = resposta.get_data(as_text=True)
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("Laboratório de Robótica", pagina)
        self.assertIn("Laboratório de Informática 1", pagina)

    def test_entrada_e_saida(self):
        dados = {
            "matricula": "2026001",
            "laboratorio": "Laboratório de Informática 1",
        }
        entrada = self.client.post("/registrar", data=dados, follow_redirects=True)
        self.assertIn("Porta aberta", entrada.get_data(as_text=True))

        saida = self.client.post("/api/acesso", json=dados)
        self.assertEqual(saida.status_code, 200)
        self.assertEqual(saida.get_json()["tipo"], "Saída")

    def test_matricula_inexistente(self):
        resposta = self.client.post(
            "/registrar",
            data={
                "matricula": "9999999",
                "laboratorio": "Laboratório de Robótica",
            },
            follow_redirects=True,
        )
        pagina = resposta.get_data(as_text=True)
        self.assertIn("Porta bloqueada", pagina)
        self.assertIn("Acesso negado", pagina)

    def test_laboratorio_invalido_na_api(self):
        resposta = self.client.post(
            "/api/acesso",
            json={"matricula": "2026001", "laboratorio": "Laboratório inexistente"},
        )
        self.assertEqual(resposta.status_code, 403)


if __name__ == "__main__":
    unittest.main()
