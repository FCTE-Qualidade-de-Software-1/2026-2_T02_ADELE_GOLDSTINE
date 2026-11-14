# Questionário com Estudantes

Esta página especifica o **questionário aplicado ao fim de cada sessão do teste com usuários**, previsto na [seção 2.3](index.md#23-instrumentos-de-coleta). Ele é a fonte da métrica M3 e de parte da lista de referência de M1 ([Métricas](metricas.md)) e complementa as medidas da sessão com a percepção do participante sobre o uso do SIGAA no dia a dia, comparando estudantes do começo e do meio ou fim do curso, conforme os [perfis da Fase 1](../fase-1/proposito-stakeholders.md#22-perfis-de-usuarios-considerados).

A versão anterior previa um questionário online anônimo, divulgado em grupos de estudantes. A equipe o substituiu por orientação da professora: um questionário sozinho é uma fonte fraca, e aplicado depois da entrevista, aos mesmos participantes, as respostas podem ser lidas junto com o que foi observado na sessão. Em troca, a amostra fica limitada aos 6 participantes do teste, e essa limitação é declarada na Fase 4.

## 1. Características do instrumento

*Tabela 1 - Características do questionário.*

| Item | Definição |
| ---- | --------- |
| Público | Os 6 participantes do teste com usuários (P1 a P6), definidos no [protocolo da Fase 3](../fase-3/teste-usuarios.md#1-participantes) |
| Formato | Em papel ou em tela separada, entregue pelo moderador no passo 7 do [roteiro da sessão](../fase-3/teste-usuarios.md#5-roteiro-da-sessao), logo após o SUS. O moderador anota o código do participante, sem o nome |
| Duração estimada | Cerca de 6 minutos (18 itens fechados e 2 abertos opcionais) |
| Validade | Só entram as respostas de participantes que assinaram o termo de consentimento da sessão |
| Dados publicados | `dados/brutos/questionario/respostas.csv`, uma linha por participante, identificada só pelo código; respostas abertas revisadas para remover qualquer dado que identifique o participante |

## 2. Consentimento

O questionário não tem termo próprio. O consentimento é obtido no início da sessão, pelo [termo de consentimento da Fase 3](../fase-3/teste-usuarios.md#5-roteiro-da-sessao), que já menciona os dois questionários respondidos ao fim. Por isso o moderador não lê nenhum texto de apresentação, apenas a instrução do passo 7 do roteiro.

## 3. Itens do questionário

As tarefas T1 a T6 são as do [escopo da Fase 1](../fase-1/escopo.md#21-tarefas-representativas). Itens marcados com (*) são obrigatórios. Os blocos mantêm a numeração original para que os códigos dos itens coincidam com as colunas do arquivo de dados; por isso não há bloco E nem item D1 (ver as notas nos blocos D e E).

### Bloco A - Perfil (cerca de 1 minuto)

| ID | Pergunta | Opções de resposta |
| -- | -------- | ------------------ |
| A1* | Você é estudante de graduação ativo(a) da UnB? | Sim / Não |
| A2* | Em qual semestre do curso você está? | 1º / 2º / 3º / 4º / 5º / 6º / 7º / 8º / 9º ou mais |
| A3* | Você prevê concluir o curso nos próximos dois semestres? | Sim / Não / Não sei |
| A4* | Em qual campus você estuda? | Darcy Ribeiro / Gama (FCTE) / Ceilândia / Planaltina |

O item A1 confirma o critério de inclusão do protocolo; um "Não" invalida a sessão inteira, não só o questionário.

### Bloco B - Acesso ao SIGAA (cerca de 1 minuto)

| ID | Pergunta | Opções de resposta |
| -- | -------- | ------------------ |
| B1* | Em qual dispositivo você mais acessa o SIGAA? | Computador ou notebook / Celular / Tablet / Uso computador e celular igualmente |
| B2* | Você tem computador (próprio ou de uso frequente) com internet para acessar o SIGAA? | Sim / Só às vezes / Não |
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

Como o participante acabou de executar as tarefas, C1 pede explicitamente a percepção "no geral", e não só na sessão; a instrução do passo 7 do roteiro reforça isso.

### Bloco D - Compreensão das informações (menos de 1 minuto)

Responda **sem consultar o SIGAA, a legenda ou outra pessoa**. Errar não tem problema: queremos saber se as informações se explicam sozinhas.

| ID | Pergunta | Opções de resposta (gabarito em negrito) |
| -- | -------- | ---------------------------------------- |
| D2* | No SIGAA, o que significa a sigla **IRA**? | **Índice de Rendimento Acadêmico** / Índice de Reprovação Acumulada / Inscrição de Registro Acadêmico / Não sei |

O item D1, que pedia a leitura do código de horário (35T23), foi retirado: o participante acabou de ver o código em T2 e respondeu a pergunta de compreensão dessa tarefa (M11), então a resposta ao questionário estaria contaminada pela sessão e repetiria M11. A sigla IRA não aparece nas tarefas da sessão, por isso D2 é mantido.

### Bloco E - Satisfação (não aplicado)

O bloco E repetia os dez itens do SUS [2]. Como o participante responde o SUS logo antes, no passo 6 do roteiro (métrica M12), o bloco não é aplicado no questionário.

### Bloco F - Ferramentas externas e funções ausentes (cerca de 1 minuto)

| ID | Pergunta | Opções de resposta |
| -- | -------- | ------------------ |
| F1* | Você usa ou já usou alguma ferramenta fora do SIGAA (site, aplicativo ou planilha) para planejar seu fluxo de disciplinas ou montar sua grade de horários? | Sim / Não |
| F2 | Se sim, qual ou quais? (marque todas) | No Fluxo UnB / Planilha própria / Outro site ou aplicativo: ____ |
| F3 | Se sim, por que você usa essa ferramenta? (marque todas) | O SIGAA não tem essa função / O SIGAA tem, mas é difícil de usar / A ferramenta mostra a informação de forma mais clara / É mais rápida / Outro: ____ |
| F4 | Que função você sente falta no SIGAA? (resposta aberta, opcional) | Texto livre |
| F5 | Quer deixar algum comentário sobre o SIGAA? (resposta aberta, opcional) | Texto livre |

## 4. Perfis usados na comparação

O semestre informado em A2 confirma o grupo do participante, definido no recrutamento pelo [protocolo da Fase 3](../fase-3/teste-usuarios.md#1-participantes). A Tabela 2 mostra a correspondência com os perfis da Fase 1.

*Tabela 2 - Grupos de comparação.*

| Grupo | Critério | Participantes | Perfil da Fase 1 |
| ----- | -------- | :-----------: | ---------------- |
| Começo do curso | A2 = 1º ou 2º semestre | 3 | Calouro |
| Meio ou fim do curso | A2 = 5º semestre ou mais | 3 | Veterano; formando quando A3 = Sim |

Estudantes do 3º e do 4º semestre não participam do teste, então não há grupo intermediário. A dependência do celular (B1 = Celular e B2 = Não ou Só às vezes) é apenas um recorte descritivo: o protocolo não recruta esse perfil, que é avaliado por inspeção em M14 e M15.

## 5. Indicadores produzidos e ligação com o GQM

O questionário alimenta a métrica M3 (com nível de pontuação) e a lista de referência de M1. Os demais itens produzem **indicadores auxiliares de percepção** (IQ1 a IQ4). Como a métrica auxiliar MA1, eles **não recebem nível de pontuação e não alteram o julgamento das características**: servem para interpretar as questões GQM, verificar a hipótese de perfil HP1 e comparar a percepção dos participantes com as medidas observadas na própria sessão.

Com 6 participantes, todos os indicadores são apresentados de forma **descritiva** (contagens, proporções e medianas), sem testes estatísticos. Em M3, cada participante equivale a cerca de 17 pontos percentuais; as faixas de [Níveis de Pontuação](niveis-pontuacao.md) não mudam, e a limitação da amostra é declarada no julgamento.

*Tabela 3 - Indicadores do questionário.*

| ID | Indicador | Itens | Cálculo | Questão GQM que complementa |
| -- | --------- | ----- | ------- | --------------------------- |
| M3 | Proporção de participantes que usam ferramentas externas | F1 | X = A/B, com A = respostas "Sim" e B = participantes com questionário válido | Q3 (métrica com nível de pontuação) |
| - | Insumo da lista de referência de M1 | F2, F3, F4 | Funções citadas, consolidadas e sem duplicatas | Q1 |
| IQ1 | Facilidade percebida por tarefa | C1.1 a C1.6 | Mediana por tarefa, ignorando "Nunca fiz"; também por grupo | Q4 e Q5; ranking das tarefas |
| IQ2 | Proporção de tarefas em que o estudante já precisou de ajuda | C2 | Tarefas marcadas / 6, por participante e por grupo | Q5 (apreensibilidade) |
| IQ3 | Acerto na interpretação da sigla IRA sem legenda | D2 | Número de acertos por grupo | Q12; complementa M11 com um termo que não aparece nas tarefas |
| IQ4 | Dependência do celular e problemas no celular | B1, B2, B5 | Número de participantes dependentes do celular; frequência de cada problema | Q15 e Q16; decisão da STI sobre interface responsiva |

## 6. Hipótese de perfil HP1

**HP1:** estudantes de 1º e 2º semestres (começo do curso) relatam menor facilidade nas tarefas (IQ1) do que estudantes a partir do 5º semestre (meio ou fim do curso).

- **Fundamento:** perfil calouro da Fase 1 (desconhece a terminologia acadêmica) e observações OP-01 e OP-04.
- **Verificação:** comparação descritiva das medianas de IQ1 por tarefa entre os dois grupos. Com três participantes por grupo, não se aplica teste estatístico.
- **Classificação na Fase 4:** tendência observada, se a mediana do grupo do começo do curso for menor na maioria das tarefas (ao menos quatro das seis); sem tendência, se for igual ou maior na maioria; inconclusiva, se algum grupo tiver menos de três questionários válidos. Em qualquer caso, o resultado é declarado como indício, não como confirmação, por causa do tamanho da amostra.

Um resultado em que os dois grupos têm a mesma dificuldade também é informativo: indica que a experiência não compensa os problemas da interface, o que reforça falhas de operabilidade e autodescritividade.

## 7. Arquivo de dados

As respostas ficam em `dados/brutos/questionario/respostas.csv`, uma linha por participante, com as colunas `participante` (P1 a P6), `a1` a `a4`, `b1`, `b2`, `b5`, `c1_1` a `c1_6`, `c2`, `d2` e `f1` a `f5`, conforme a [página Planilhas de Coleta](../fase-3/planilhas.md#4-questionario). O cálculo dos indicadores será registrado em script ou planilha versionada, conforme a premissa 5 do roteiro.

## Referências

[1] SAURO, J.; LEWIS, J. R. *Quantifying the User Experience: Practical Statistics for User Research*. 2. ed. Cambridge: Morgan Kaufmann, 2016.

[2] BROOKE, J. SUS: a "quick and dirty" usability scale. In: JORDAN, P. W. et al. (ed.). *Usability Evaluation in Industry*. Londres: Taylor & Francis, 1996. p. 189-194.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 19/10/2026 | Especificação do questionário: termo de consentimento, itens dos blocos A a F, grupos de comparação, indicadores IQ1 a IQ6 e hipótese de perfil HP1 | [arthurlleite](https://github.com/arthurlleite) |
| 1.1 | 25/10/2026 | Remoção dos itens B3 e B4 e do indicador IQ6, ligados ao objetivo G4 (Eficiência de Desempenho) | Leonardo Bonetti |
| 1.2 | 25/10/2026 | Questões GQM complementadas pelos indicadores IQ3 a IQ5 na numeração Q1 a Q16 | Leonardo Bonetti |
| 1.3 | 14/11/2026 | Questionário aplicado ao fim da sessão do teste com usuários, no lugar do questionário online: público P1 a P6, consentimento pelo termo da sessão, retirada do item D1 e do bloco E, dois grupos iguais aos do protocolo, indicadores IQ1 a IQ4 descritivos e HP1 com comparação descritiva | Caio Borges |
