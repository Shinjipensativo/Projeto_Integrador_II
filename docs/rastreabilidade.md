# Rastreabilidade - AcessoLab

## Objetivo

Relacionar as tarefas do Trello às Issues, commits e arquivos correspondentes no GitHub.

## Procedimento

1. Criar ou atualizar a Issue correspondente;
2. anexar seu link ao cartão do Trello;
3. realizar e testar a tarefa;
4. criar um commit mencionando a Issue;
5. colar o link do commit no cartão;
6. atualizar a situação na tabela.

## Padrão de commits

| Tipo | Exemplo |
|---|---|
| Funcionalidade | `feat: adiciona simulacao virtual da porta (#1)` |
| Correção | `fix: corrige registro do laboratorio (#2)` |
| Teste | `test: adiciona validacao do controle de acesso (#3)` |
| Documentação | `docs: atualiza entrega da etapa 3 (#4)` |

## Tabela da Etapa 3

| Tarefa | Responsável | Issue do GitHub | Arquivo principal | Situação |
|---|---|---|---|---|
| Finalizar a plataforma web | Fredy | [Issue #1](https://github.com/Shinjipensativo/Projeto_Integrador_II/issues/1) | `src/web/app.py` | Em revisão |
| Finalizar o design da plataforma | Fredy | [Issue #2](https://github.com/Shinjipensativo/Projeto_Integrador_II/issues/2) | `src/web/templates` e `src/web/static` | Concluído |
| Desenvolver a simulação virtual | Fredy | [Issue #3](https://github.com/Shinjipensativo/Projeto_Integrador_II/issues/3) | `src/web/templates/inicio.html` | Em revisão |
| Validar e documentar o protótipo | Fredy | [Issue #4](https://github.com/Shinjipensativo/Projeto_Integrador_II/issues/4) | `docs/testes.md` | Em revisão |
| Preparar a entrega final | Fredy | [Issue #5](https://github.com/Shinjipensativo/Projeto_Integrador_II/issues/5) | Release `v1.0.0` | Em andamento |
