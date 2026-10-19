# Questionário com Estudantes

Esta página especifica o **questionário online anônimo** previsto na [seção 2.3](index.md#23-instrumentos-de-coleta). Ele é a fonte da métrica M3 e de parte da lista de referência de M1 ([Métricas](metricas.md)) e amplia a amostra do teste com usuários para **comparar estudantes em diferentes momentos do curso**, sobretudo calouros e veteranos, conforme os [perfis da Fase 1](../fase-1/proposito-stakeholders.md#22-perfis-de-usuarios-considerados).

## 1. Características do instrumento

*Tabela 1 - Características do questionário.*

| Item | Definição |
| ---- | --------- |
| Público | Estudantes de graduação ativos da UnB, de qualquer curso e campus |
| Formato | Formulário online (Google Forms ou equivalente), sem coleta de e-mail, nome ou matrícula |
| Duração estimada | 5 a 8 minutos (31 itens fechados e 2 abertos opcionais) |
| Divulgação | Grupos de estudantes, centros acadêmicos e listas de turmas, durante a janela de coleta da Fase 4 |
| Amostra-alvo | Ao menos 60 respostas válidas, com ao menos 15 por perfil (calouro, intermediário e veterano) |
| Validade | Só são consideradas as respostas com "Sim" no item A1 e com o termo de consentimento aceito |
| Dados publicados | Planilha anonimizada em `dados/brutos/questionario/respostas.csv`; respostas abertas revisadas para remover qualquer dado que identifique o respondente |

## 2. Termo de consentimento (abertura do formulário)

> Este questionário faz parte de um trabalho da disciplina Qualidade de Software 1 (FCTE/UnB), que avalia a qualidade do SIGAA do ponto de vista do estudante. A participação é voluntária e anônima: não pedimos nome, e-mail nem matrícula. As respostas serão usadas apenas de forma agregada e publicadas, sem identificação, no repositório do projeto. Você pode desistir a qualquer momento, sem prejuízo. O preenchimento leva de 5 a 8 minutos.
>
> ( ) Li e concordo em participar.

## 3. Itens do questionário

As tarefas T1 a T6 são as do [escopo da Fase 1](../fase-1/escopo.md#21-tarefas-representativas). Itens marcados com (*) são obrigatórios.

### Bloco A - Perfil (cerca de 1 minuto)

| ID | Pergunta | Opções de resposta |
| -- | -------- | ------------------ |
| A1* | Você é estudante de graduação ativo(a) da UnB? | Sim / Não (encerra o formulário) |
| A2* | Em qual semestre do curso você está? | 1º / 2º / 3º / 4º / 5º / 6º / 7º / 8º / 9º ou mais |
| A3* | Você prevê concluir o curso nos próximos dois semestres? | Sim / Não / Não sei |
| A4* | Em qual campus você estuda? | Darcy Ribeiro / Gama (FCTE) / Ceilândia / Planaltina |

### Bloco B - Acesso ao SIGAA (cerca de 1 minuto)

| ID | Pergunta | Opções de resposta |
| -- | -------- | ------------------ |
| B1* | Em qual dispositivo você mais acessa o SIGAA? | Computador ou notebook / Celular / Tablet / Uso computador e celular igualmente |
| B2* | Você tem computador (próprio ou de uso frequente) com internet para acessar o SIGAA? | Sim / Só às vezes / Não |
| B3* | Que conexão você mais usa para acessar o SIGAA? | Wi-Fi de casa / Wi-Fi da UnB / Dados móveis do celular |
| B4* | Com que frequência o SIGAA parece lento para você? | Nunca / Raramente / Às vezes / Frequentemente / Sempre |
| B5* | Quando usa o SIGAA no celular, quais problemas você já teve? (marque todos que se aplicam) | Precisei dar zoom ou rolar para o lado / Um menu não abriu ao tocar / Botões ou links pequenos demais / Conteúdo cortado ou sobreposto / Não consegui concluir o que queria / Nenhum problema / Não uso o SIGAA no celular |

### Bloco C - Facilidade das tarefas (cerca de 2 minutos)

**C1.** *No geral, quão fácil ou difícil é para você realizar cada tarefa no SIGAA?* Escala de 1 (muito difícil) a 5 (muito fácil), com a opção "Nunca fiz". Formato de grade, uma linha por tarefa (adaptação da *Single Ease Question*, SEQ [1]).

| ID | Tarefa |
| -- | ------ |
| C1.1* | Consultar as notas de uma disciplina (T1) |
| C1.2* | Descobrir o dia, o horário e a sala de uma turma (T2) |
| C1.3* | Emitir atestado de matrícula ou histórico escolar (T3) |
| C1.4* | Verificar quantas horas faltam para se formar (T4) |
| C1.5* | Encontrar um material publicado pelo professor na Turma Virtual (T5) |
| C1.6* | Consultar o calendário acadêmico, por exemplo, o prazo de trancamento (T6) |

| ID | Pergunta | Opções de resposta |
| -- | -------- | ------------------ |
| C2* | Em quais dessas tarefas você já precisou pedir ajuda (a colegas, vídeos ou tutoriais) para conseguir fazer? (marque todas) | T1 / T2 / T3 / T4 / T5 / T6 / Nenhuma |

### Bloco D - Compreensão das informações (cerca de 1 minuto)

Responda **sem consultar o SIGAA, a legenda ou outra pessoa**. Errar não tem problema: queremos saber se as informações se explicam sozinhas.

| ID | Pergunta | Opções de resposta (gabarito em negrito) |
| -- | -------- | ---------------------------------------- |
| D1* | No SIGAA, uma turma aparece com o horário **35T23**. O que isso significa? | **Aulas às terças e quintas-feiras, à tarde** / Aulas às quartas e sextas-feiras, à tarde / Turma 35, na sala T23 / Aulas nos dias 3 e 5 de cada mês, às 23h / Não sei |
| D2* | No SIGAA, o que significa a sigla **IRA**? | **Índice de Rendimento Acadêmico** / Índice de Reprovação Acumulada / Inscrição de Registro Acadêmico / Não sei |

No código de horário do SIGAA, os primeiros dígitos indicam os dias da semana (2 = segunda, 3 = terça, 4 = quarta, 5 = quinta, 6 = sexta, 7 = sábado), a letra indica o turno (M = manhã, T = tarde, N = noite) e os últimos dígitos indicam os horários dentro do turno. Os distratores representam leituras plausíveis de quem não conhece a notação: contar a semana a partir de segunda = 1, ler o código como número de turma e sala, ou como datas.

### Bloco E - Satisfação: System Usability Scale (cerca de 2 minutos)

*Pensando no seu uso do SIGAA, indique o quanto você concorda com cada afirmação.* Escala de 1 (discordo totalmente) a 5 (concordo totalmente). Versão em português dos dez itens de Brooke [2].

| ID | Afirmação |
| -- | --------- |
| E1* | Eu acho que gostaria de usar este sistema com frequência. |
| E2* | Eu achei o sistema desnecessariamente complexo. |
| E3* | Eu achei o sistema fácil de usar. |
| E4* | Eu acho que precisaria do apoio de alguém com conhecimento técnico para usar este sistema. |
| E5* | Eu achei que as várias funções do sistema estão bem integradas. |
| E6* | Eu achei que o sistema tem muita inconsistência. |
| E7* | Eu imagino que a maioria das pessoas aprenderia a usar este sistema rapidamente. |
| E8* | Eu achei o sistema muito complicado de usar. |
| E9* | Eu me senti muito confiante usando o sistema. |
| E10* | Eu precisei aprender várias coisas antes de conseguir usar este sistema. |

O item E1 é mantido na forma original para preservar a comparabilidade com a média de referência do SUS, embora o uso do SIGAA seja obrigatório; esse efeito é discutido como limitação na Fase 4.

### Bloco F - Ferramentas externas e funções ausentes (cerca de 1 minuto)

| ID | Pergunta | Opções de resposta |
| -- | -------- | ------------------ |
| F1* | Você usa ou já usou alguma ferramenta fora do SIGAA (site, aplicativo ou planilha) para planejar seu fluxo de disciplinas ou montar sua grade de horários? | Sim / Não |
| F2 | Se sim, qual ou quais? (marque todas) | No Fluxo UnB / Planilha própria / Outro site ou aplicativo: ____ |
| F3 | Se sim, por que você usa essa ferramenta? (marque todas) | O SIGAA não tem essa função / O SIGAA tem, mas é difícil de usar / A ferramenta mostra a informação de forma mais clara / É mais rápida / Outro: ____ |
| F4 | Que função você sente falta no SIGAA? (resposta aberta, opcional) | Texto livre |
| F5 | Quer deixar algum comentário sobre o SIGAA? (resposta aberta, opcional) | Texto livre |

## 4. Perfis usados na comparação

O semestre informado em A2 define o grupo de comparação. A Tabela 2 mostra a correspondência com os perfis da Fase 1.

*Tabela 2 - Grupos de comparação.*

| Grupo | Critério | Perfil da Fase 1 |
| ----- | -------- | ---------------- |
| Calouro | A2 = 1º ou 2º semestre | Calouro |
| Intermediário | A2 = 3º ou 4º semestre | (grupo de transição, apresentado apenas de forma descritiva) |
| Veterano | A2 = 5º semestre ou mais | Veterano; formando quando A3 = Sim |
| Dependente do celular | B1 = Celular e B2 = Não ou Só às vezes | Estudante que acessa apenas pelo celular |

## 5. Indicadores produzidos e ligação com o GQM

O questionário alimenta a métrica M3 (com nível de pontuação) e a lista de referência de M1. Os demais itens produzem **indicadores auxiliares de percepção** (IQ1 a IQ6). Como a métrica auxiliar MA1, eles **não recebem nível de pontuação e não alteram o julgamento das características**: servem para interpretar as questões GQM, verificar a hipótese de perfil HP1 e comparar a percepção dos estudantes com as medidas observadas no teste com usuários.

*Tabela 3 - Indicadores do questionário.*

| ID | Indicador | Itens | Cálculo | Questão GQM que complementa |
| -- | --------- | ----- | ------- | --------------------------- |
| M3 | Proporção de estudantes que usam ferramentas externas | F1 | X = A/B, com A = respostas "Sim" e B = respostas válidas | Q3 (métrica com nível de pontuação) |
| - | Insumo da lista de referência de M1 | F2, F3, F4 | Funções citadas, consolidadas e sem duplicatas | Q1 |
| IQ1 | Facilidade percebida por tarefa | C1.1 a C1.6 | Mediana e média por tarefa, ignorando "Nunca fiz"; também por grupo | Q4 e Q5; ranking das tarefas |
| IQ2 | Proporção de tarefas em que o estudante já precisou de ajuda | C2 | Tarefas marcadas / 6, média por grupo | Q5 (apreensibilidade) |
| IQ3 | Acerto na interpretação sem legenda | D1, D2 | Proporção de respostas corretas por item e por grupo | Q9; compara com M11 |
| IQ4 | SUS do questionário | E1 a E10 | Mesmo cálculo de M12 (0 a 100), média por grupo | Q10; compara com M12 |
| IQ5 | Dependência do celular e problemas no celular | B1, B2, B5 | Proporção de dependentes do celular; frequência de cada problema | Q12; decisão da STI sobre interface responsiva |
| IQ6 | Lentidão percebida | B3, B4 | Proporção de "Frequentemente" ou "Sempre", por tipo de conexão | Q13; hipótese de relação HR4 |

## 6. Hipótese de perfil HP1

**HP1:** estudantes de 1º e 2º semestres (calouros) relatam menor facilidade nas tarefas (IQ1) e acertam menos a interpretação do código de horário (IQ3, item D1) do que estudantes a partir do 5º semestre (veteranos).

- **Fundamento:** perfil calouro da Fase 1 (desconhece a terminologia acadêmica) e observações OP-01 e OP-04.
- **Verificação:** comparação das medianas de IQ1 e da proporção de acerto em D1 entre os grupos. Se cada grupo tiver ao menos dez respondentes, aplica-se o teste de Mann-Whitney para IQ1 e o teste exato de Fisher para D1, com nível de significância de 5%; caso contrário, a comparação é apenas descritiva.
- **Classificação na Fase 4:** confirmada, se as duas diferenças ocorrerem na direção esperada e forem significativas; refutada, se alguma diferença for significativa na direção oposta ou se não houver diferença; inconclusiva, se algum grupo tiver menos de dez respondentes.

Um resultado em que calouros e veteranos têm a mesma dificuldade também é informativo: indica que a experiência não compensa os problemas da interface, o que reforça falhas de operabilidade e autodescritividade.

## 7. Arquivo de dados

As respostas exportadas ficam em `dados/brutos/questionario/respostas.csv`, uma linha por resposta válida, com as colunas `id` (R001, R002, ...), `data`, `A1` a `A4`, `B1` a `B5`, `C1_1` a `C1_6`, `C2`, `D1`, `D2`, `E1` a `E10` e `F1` a `F5`. O cálculo dos indicadores será registrado em script ou planilha versionada, conforme a premissa 5 do roteiro.

## Referências

[1] SAURO, J.; LEWIS, J. R. *Quantifying the User Experience: Practical Statistics for User Research*. 2. ed. Cambridge: Morgan Kaufmann, 2016.

[2] BROOKE, J. SUS: a "quick and dirty" usability scale. In: JORDAN, P. W. et al. (ed.). *Usability Evaluation in Industry*. Londres: Taylor & Francis, 1996. p. 189-194.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 19/10/2026 | Especificação do questionário: termo de consentimento, itens dos blocos A a F, grupos de comparação, indicadores IQ1 a IQ6 e hipótese de perfil HP1 | Arthur Leite |
