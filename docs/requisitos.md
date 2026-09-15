# Requisitos do AcessoLab

## Requisitos funcionais

| Código | Requisito | Situação |
|---|---|---|
| RF01 | Cadastrar alunos, matrículas e turmas. | Implementado |
| RF02 | Validar a matrícula informada. | Implementado |
| RF03 | Registrar data e horário de entrada e saída. | Implementado |
| RF04 | Simular a abertura da porta para usuários autorizados. | Implementado |
| RF05 | Negar acesso a matrículas não cadastradas ou inativas. | Implementado |
| RF06 | Permitir a consulta ao histórico de acessos. | Implementado |
| RF07 | Permitir a seleção do laboratório. | Implementado |
| RF08 | Exibir sinais visuais conforme o resultado. | Implementado |
| RF09 | Permitir ativar ou desativar o cadastro de um aluno. | Implementado |

## Requisitos não funcionais

| Código | Requisito |
|---|---|
| RNF01 | O sistema deverá apresentar a resposta em poucos segundos. |
| RNF02 | As mensagens deverão ser simples e compreensíveis. |
| RNF03 | Os dados deverão permanecer armazenados após o encerramento. |
| RNF04 | A interface deverá funcionar em computadores e telas menores. |
| RNF05 | O sistema deverá ser fácil de executar, utilizar e manter. |
| RNF06 | As consultas deverão utilizar parâmetros para reduzir riscos de injeção SQL. |

## Limitações da versão

- A abertura da porta é apenas visual;
- não existe ESP32 ou circuito conectado;
- a aplicação é executada localmente;
- não há autenticação administrativa nesta demonstração;
- não há integração com o banco institucional da escola.

---

**Projeto:** AcessoLab  
**Versão:** 1.0.0  
**Ano:** 2026
