# AcessoLab

Sistema acadêmico de controle de entrada e saída para laboratórios de Informática e Robótica do CTBJ.

## Situação-problema

O controle de frequência nos laboratórios costuma ser realizado manualmente. Alguns alunos entram sem assinar a lista, dificultando a identificação de quem utilizou o ambiente e em qual horário.

## Proposta de solução

O AcessoLab permite cadastrar alunos, validar a matrícula, selecionar o laboratório e registrar entradas e saídas. Nesta versão, a abertura da porta e os sinais luminosos são representados por uma **simulação virtual na plataforma web**.

> O professor autorizou a entrega como protótipo virtual. Não houve montagem nem validação com ESP32 nesta versão.

## Funcionalidades

- Cadastro de alunos, matrícula e turma;
- ativação e desativação de cadastros;
- seleção entre Robótica, Informática 1 e Informática 2;
- validação da matrícula;
- registro automático de entrada ou saída;
- simulação visual da abertura da porta;
- sinal verde para acesso autorizado e vermelho para acesso negado;
- listagem de alunos presentes;
- histórico com busca por aluno, matrícula ou laboratório;
- armazenamento local em SQLite;
- rota de API preparada para integração futura.

## Tecnologias

| Área | Tecnologia |
|---|---|
| Linguagem | Python |
| Servidor web | Flask |
| Banco de dados | SQLite |
| Interface | HTML e CSS |
| Gestão | Trello |
| Versionamento | GitHub |

## Estrutura

```text
AcessoLab/
├── docs/
│   ├── arquitetura.md
│   ├── backlog-etapa-3.md
│   ├── checklist-etapa-3.md
│   ├── rastreabilidade.md
│   ├── requisitos.md
│   └── testes.md
├── src/web/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   └── requirements.txt
├── .gitignore
└── README.md
```

## Como executar no Windows

É necessário ter o Python 3 instalado. Abra o terminal na pasta do projeto e execute:

```bash
cd src\web
python -m pip install -r requirements.txt
python app.py
```

Se `python` não funcionar, utilize `py`. Depois, acesse `http://127.0.0.1:5000`. O banco `acessolab.db` será criado automaticamente. Para encerrar, pressione `Ctrl + C`.

## Como demonstrar

1. Abra **Alunos** e cadastre um estudante;
2. retorne ao painel e selecione um laboratório;
3. digite uma matrícula cadastrada;
4. observe a porta virtual aberta e o sinal verde;
5. repita a matrícula no mesmo laboratório para registrar a saída;
6. teste uma matrícula inexistente para visualizar a porta bloqueada;
7. abra **Histórico** para conferir os registros.

## Resultados

O protótipo demonstra o fluxo essencial inteiramente por software: valida os cadastros, registra as movimentações e representa visualmente a resposta que futuramente poderia ser enviada ao mecanismo físico.

Os testes e espaços destinados às evidências estão em [`docs/testes.md`](docs/testes.md).

## Melhorias futuras

- Integração com ESP32, teclado matricial e servo motor;
- autenticação de administradores;
- exportação de relatórios;
- hospedagem em servidor institucional;
- integração com sistemas acadêmicos;
- leitor biométrico, mediante autorização e adequação à proteção de dados.

## Links

- [Repositório no GitHub](https://github.com/Shinjipensativo/Projeto_Integrador_II)
- [Quadro no Trello](https://trello.com/b/0ssTbj1k/acessolab-projeto-integrador-ii)

## Autor

**Fredy Gomes Martins** - 3º ano B - Curso Técnico em Informática - CTBJ.

**Versão:** 1.0.0  
**Ano:** 2026
