# Plataforma Web do AcessoLab

Protótipo virtual desenvolvido com Python, Flask e SQLite. Cadastra alunos, valida matrículas, registra entradas e saídas por laboratório e simula visualmente a abertura da porta.

## Execução no Windows

```bash
python -m pip install -r requirements.txt
python app.py
```

Se necessário, substitua `python` por `py`. Depois, acesse `http://127.0.0.1:5000`.

## Teste manual

1. Cadastre um aluno em **Alunos**;
2. selecione um laboratório;
3. informe a matrícula para registrar a entrada;
4. confira a porta virtual aberta e o sinal verde;
5. repita a matrícula para registrar a saída;
6. informe uma matrícula inexistente e confira o sinal vermelho;
7. consulte a página **Histórico**.

## API futura

Envie `POST /api/acesso` com:

```json
{
  "matricula": "2026001",
  "laboratorio": "Laboratório de Robótica"
}
```

> A versão atual é uma demonstração local. Não houve montagem ou teste com ESP32.

## Testes automatizados

Dentro desta pasta, execute:

```bash
python -m unittest discover -s tests -v
```
