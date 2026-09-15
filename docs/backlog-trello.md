# Backlog e Organização do Trello - AcessoLab

> Este arquivo registra o planejamento da Etapa 2. Na Etapa 3, o professor autorizou que o produto fosse finalizado como protótipo virtual. Por isso, as tarefas atuais estão em `backlog-etapa-3.md` e a montagem física ficou como melhoria futura.

## 1. Estrutura do quadro

Criar um quadro chamado **AcessoLab - Projeto Integrador II** com as colunas:

1. **A Fazer**;
2. **Em Andamento**;
3. **Em Revisão**;
4. **Concluído**.

## 2. Etiquetas

| Etiqueta | Cor sugerida | Significado |
|---|---|---|
| Prioridade alta | Vermelha | Tarefa essencial ou urgente. |
| Prioridade média | Amarela | Tarefa importante, mas não bloqueadora. |
| Prioridade baixa | Verde | Melhoria ou complemento. |
| Hardware | Roxa | Atividade do protótipo físico. |
| Software | Azul | Atividade do sistema ou código. |
| Documentação | Cinza | Relatórios, diagramas e GitHub. |

## 3. Modelo de cartão

Cada cartão deverá possuir:

- título;
- descrição do que será realizado;
- responsável;
- data de entrega;
- etiqueta de prioridade e área;
- checklist;
- link da Issue ou do commit correspondente no GitHub.

## 4. Cartões do backlog

### Cartão 01 - Definir os componentes do protótipo

**Descrição:** Confirmar os componentes necessários para a montagem da maquete do AcessoLab.  
**Responsável:** Fredy Gomes Martins  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade alta / Hardware

**Checklist:**

- [ ] Confirmar o uso do ESP32;
- [ ] confirmar teclado matricial e servo;
- [ ] verificar display, LEDs e buzzer;
- [ ] registrar a lista no relatório de arquitetura.

### Cartão 02 - Criar o diagrama da arquitetura

**Descrição:** Representar a comunicação entre aluno, teclado, ESP32, sistema web e banco de dados.  
**Responsável:** **[Integrante 2]**  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade alta / Documentação

**Checklist:**

- [ ] Criar o diagrama;
- [ ] revisar o fluxo;
- [ ] adicionar em `docs/arquitetura.md`;
- [ ] enviar o commit ao GitHub.

### Cartão 03 - Criar o fluxograma de acesso

**Descrição:** Modelar a validação da matrícula e o registro de entrada ou saída.  
**Responsável:** **[Integrante 3]**  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade alta / Documentação

**Checklist:**

- [ ] Representar matrícula válida e inválida;
- [ ] representar entrada e saída;
- [ ] representar a liberação do servo;
- [ ] inserir o fluxograma no relatório.

### Cartão 04 - Elaborar o modelo do banco de dados

**Descrição:** Definir as tabelas de alunos e acessos e o relacionamento entre elas.  
**Responsável:** Fredy Gomes Martins  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade alta / Software

**Checklist:**

- [ ] Definir os campos da tabela de alunos;
- [ ] definir os campos da tabela de acessos;
- [ ] criar o diagrama entidade-relacionamento;
- [ ] adicionar o modelo ao relatório.

### Cartão 05 - Criar os protótipos das telas

**Descrição:** Esboçar a tela de acesso, o painel do responsável e o cadastro de alunos.  
**Responsável:** **[Integrante 2]**  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade média / Software

**Checklist:**

- [ ] Esboçar a tela de acesso;
- [ ] esboçar o painel;
- [ ] esboçar o cadastro;
- [ ] inserir imagens ou descrição no relatório.

### Cartão 06 - Planejar a montagem da maquete

**Descrição:** Definir o formato da porta, o local dos componentes e as conexões do circuito.  
**Responsável:** **[Integrante 3]**  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade média / Hardware

**Checklist:**

- [ ] Escolher o material da maquete;
- [ ] definir a posição do servo;
- [ ] definir a posição do teclado e do display;
- [ ] desenhar um esquema inicial.

### Cartão 07 - Planejar a programação do ESP32

**Descrição:** Dividir o código do ESP32 nas funções de leitura, comunicação e acionamento.  
**Responsável:** Fredy Gomes Martins  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade alta / Hardware / Software

**Checklist:**

- [ ] Planejar a leitura do teclado;
- [ ] planejar a conexão Wi-Fi;
- [ ] planejar o envio da matrícula;
- [ ] planejar o controle do servo e dos avisos.

### Cartão 08 - Planejar o sistema web

**Descrição:** Definir as funções e páginas necessárias ao sistema de gerenciamento.  
**Responsável:** **[Integrante 2]**  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade alta / Software

**Checklist:**

- [ ] Definir cadastro de alunos;
- [ ] definir consulta ao histórico;
- [ ] definir lista de alunos presentes;
- [ ] definir comunicação com o ESP32.

### Cartão 09 - Revisar a documentação da Etapa 2

**Descrição:** Conferir diagramas, responsáveis, prazos, cartões e arquivos do GitHub.  
**Responsável:** **[Integrante 3]**  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade alta / Documentação

**Checklist:**

- [ ] Revisar `arquitetura.md`;
- [ ] revisar os cartões do Trello;
- [ ] verificar os responsáveis e prazos;
- [ ] verificar os links de rastreabilidade.

### Cartão 10 - Preparar a entrega da Etapa 2

**Descrição:** Reunir os links e verificar se todas as exigências do guia foram cumpridas.  
**Responsável:** Fredy Gomes Martins  
**Prazo:** **[data]**  
**Etiquetas:** Prioridade alta / Documentação

**Checklist:**

- [ ] Confirmar o convite do professor no Trello;
- [ ] confirmar o acesso ao repositório;
- [ ] verificar a pasta `docs`;
- [ ] enviar os links solicitados.

## 5. Estado inicial sugerido

Coloque inicialmente todos os cartões em **A Fazer**. Quando alguém começar uma atividade, mova o cartão para **Em Andamento**. Depois, outro integrante deverá conferir e movê-lo para **Em Revisão**. Somente após a conferência o cartão deverá ir para **Concluído**.
