# Hipóteses

## Como as hipóteses são formuladas e classificadas

Cada questão tem uma hipótese (H1 a H14 ↔ Q1 a Q14) que declara, **antes da coleta**, a resposta esperada. A hipótese é expressa como o nível esperado de cada métrica da questão, com um critério de confirmação numérico que usa as faixas de [Níveis de Pontuação](niveis-pontuacao.md#faixas-por-metrica). Cada hipótese indica seu fundamento na Fase 1: as observações preliminares OP-01 a OP-08 ([Software Avaliado](../fase-1/software-avaliado.md#4-observacoes-preliminares-da-interface)) ou a justificativa das notas da [matriz Impacto x Risco](../fase-1/caracteristicas.md#21-justificativa-das-notas).

Na Fase 4, cada hipótese será classificada como:

- **Confirmada:** todas as métricas do critério de confirmação ficaram nas faixas esperadas;
- **Refutada:** ao menos uma métrica com dados ficou fora da faixa esperada;
- **Inconclusiva:** ao menos uma métrica do critério ficou sem dados suficientes (métrica não aplicável, regra 1, ou recorte com menos de três participantes, regra 3 de [Níveis de Pontuação](niveis-pontuacao.md#regras-complementares)), e as demais não bastam para refutar a hipótese.

Uma hipótese refutada não é uma falha da avaliação: ela indica que a percepção registrada na Fase 1 não se confirmou e é discutida na Fase 4.

## G1 - Adequação Funcional

*Tabela 1 - Hipóteses do objetivo G1 - Adequação Funcional.*

| ID | Questão | Hipótese | Critério de confirmação |
| -- | ------- | -------- | ----------------------- |
| H1 | Q1 | A cobertura funcional fica entre 75% e 90%, com o pior resultado em T4 (integralização) e nas funções de planejamento do fluxo, oferecidas por ferramentas da comunidade e ausentes no SIGAA. Fundamento: OP-07. | M1 ≥ 75% e < 90% (Regular) |
| H2 | Q2 | Não há divergência entre os dados exibidos pelo SIGAA, as fontes oficiais e os documentos emitidos pelo próprio sistema. Fundamento: justificativa R = 4 de Adequação Funcional ("não há indício forte de problemas de correção"). | M2 = 100% (Excelente) |
| H3 | Q3 | Entre um quarto e metade dos respondentes usa alguma ferramenta externa para planejar o fluxo ou a grade de horários, porque o SIGAA não oferece simulação do fluxo. Fundamento: OP-07; justificativa R = 4 de Adequação Funcional (lacunas de completude). | M3 > 25% e ≤ 50% (Regular) |

## G2 - Capacidade de Interação (Usabilidade)

*Tabela 2 - Hipóteses do objetivo G2 - Capacidade de Interação.*

| ID | Questão | Hipótese | Critério de confirmação |
| -- | ------- | -------- | ----------------------- |
| H4 | Q4 | Entre 50% e 75% das tentativas começam com a primeira escolha de menu correta, porque o menu Ensino reúne cerca de 20 itens de naturezas diferentes em um único nível. Fundamento: OP-04. | M4 ≥ 50% e < 75% (Regular) |
| H5 | Q5 | Os estudantes concluem a maior parte das tarefas sem ajuda, mas os calouros, por desconhecerem a terminologia acadêmica e a organização dos menus, concluem menos de 65% das tarefas no primeiro contato. Fundamento: OP-01 e OP-04; perfil calouro. | M5 ≥ 78% e < 90% (Bom); no recorte de calouros, com ao menos três participantes, M5 < 65% (Regular ou Insatisfatório) |
| H6 | Q6 | Os participantes que concluem as tarefas gastam bem mais tempo e cliques que o especialista, por causa do menu extenso e das duas estruturas de navegação: o sistema é usável, porém trabalhoso. Fundamento: OP-04 e OP-05; justificativa R = 5 de Capacidade de Interação. | M6 > 2,5 e ≤ 4,0 (Regular) e M7 > 1,33 e ≤ 2,00 (Regular); Q6 Regular |
| H7 | Q7 | O sistema trata no máximo dois dos seis cenários de erro previstos, falhando sobretudo no uso do botão Voltar do navegador e na expiração da sessão, e os estudantes se recuperam sem ajuda e sem retrabalho de 50% a 70% dos erros. Fundamento: OP-06. | M20 < 50%, isto é, 0 a 2 cenários tratados (Insatisfatório), e M8 ≥ 50% e < 70% (Regular); Q7 Insatisfatório |
| H8 | Q8 | As páginas têm erros automáticos de acessibilidade frequentes, como campos sem rótulo e links sem texto, típicos de uma interface antiga com muitos elementos, mas parte dos critérios manuais é atendida, com apoio do recurso de ampliação de fonte (A+/A-). Fundamento: OP-08 (ponto positivo); justificativa R = 4 de Eficiência de Desempenho (páginas JSF com muitos elementos). | M9 > 5 erros por página (Insatisfatório) e M10 ≥ 75% e < 90%, isto é, 18 a 21 das 24 verificações (Regular); Q8 Insatisfatório |
| H9 | Q9 | A pergunta sobre o código de horário de T2 tem menos de 50% de acertos sem legenda, e o conjunto das três perguntas de compreensão fica entre 50% e 75%. Fundamento: OP-01. | M11 ≥ 50% e < 75% (Regular), com a pergunta de T2 abaixo de 50% no resultado por pergunta |
| H10 | Q10 | A pontuação SUS média fica entre 51 e 68, abaixo da média de referência dos sistemas avaliados com o questionário. Fundamento: justificativa R = 5 de Capacidade de Interação (queixa mais frequente entre os colegas). | M12 ≥ 51 e < 68 (Regular) |

## G3 - Flexibilidade (Portabilidade)

*Tabela 3 - Hipóteses do objetivo G3 - Flexibilidade.*

| ID | Questão | Hipótese | Critério de confirmação |
| -- | ------- | -------- | ----------------------- |
| H11 | Q11 | As tarefas funcionam nos quatro navegadores de computador, com falhas pontuais em no máximo duas combinações, como a geração do documento em PDF de T3 em um navegador que bloqueia a janela. Os problemas de flexibilidade registrados na Fase 1 dizem respeito a telas pequenas e ao toque e são tratados em Q12. Fundamento: justificativa R = 4 de Flexibilidade, baseada em OP-02 e OP-03, que não afetam o computador. | M13 ≥ 90% e < 100%, isto é, 22 ou 23 das 24 combinações (Bom) |
| H12 | Q12 | Menos da metade das verificações página × largura é adaptada, por causa do layout de largura fixa e dos menus abertos pela passagem do ponteiro, e as tarefas no celular levam entre 1,5 e 2 vezes o tempo no computador. Fundamento: OP-02 e OP-03. | M14 < 50%, isto é, 5 ou menos das 12 verificações (Insatisfatório), e M15 > 1,5 e ≤ 2,0 (Regular); Q12 Insatisfatório |

## G4 - Eficiência de Desempenho

*Tabela 4 - Hipóteses do objetivo G4 - Eficiência de Desempenho.*

| ID | Questão | Hipótese | Critério de confirmação |
| -- | ------- | -------- | ----------------------- |
| H13 | Q13 | Em rede comum, o conteúdo principal das páginas aparece em até 2,5 s, mas em rede móvel simulada passa de 2,5 s. Fundamento: justificativa R = 4 de Eficiência de Desempenho (interface JSF com muitos elementos e requisições; lentidão relatada). | M16 > 1,0 e ≤ 2,5 s (Bom) e M17 > 2,5 s (Regular ou Insatisfatório); Q13 Regular ou Insatisfatório |
| H14 | Q14 | As páginas são moderadamente pesadas (até 1 MB), mas exigem muitas requisições (mais de 50), por carregarem scripts e folhas de estilo do framework em cada página. Fundamento: justificativa R = 4 de Eficiência de Desempenho. | M18 > 0,5 e ≤ 1,0 MB (Bom) e M19 > 50 e ≤ 80 (Regular); Q14 Regular |

## Hipóteses de relação entre as características

O roteiro exige discutir, ao final, as relações entre as características (premissa 1). As relações esperadas da [Fase 1](../fase-1/caracteristicas.md#5-relacoes-esperadas-entre-as-caracteristicas) foram convertidas em hipóteses verificáveis (Tabela 5), usando as métricas indicadas na [visão geral](index.md#24-relacoes-entre-as-caracteristicas). Essas hipóteses não recebem nível de pontuação; elas são declaradas estabelecidas ou não estabelecidas na Fase 4.

*Tabela 5 - Hipóteses de relação e forma de verificação.*

| ID | Relação | Hipótese | Como será verificada | Condição para considerar a relação não estabelecida |
| -- | ------- | -------- | -------------------- | --------------------------------------------------- |
| HR1 | Flexibilidade → Capacidade de Interação | No celular, as tarefas exigem mais esforço do que no computador, e o esforço adicional se concentra nas tarefas cujas páginas não são adaptadas. Se houver sessões do teste com usuários no celular, M5 e M6 ficam ao menos um nível abaixo do resultado em computador. | M15 por tarefa, cruzado com o resultado de M14 da página de cada tarefa; comparação complementar de M5 e M6 entre as sessões em computador e em celular, por tarefa | M15 ≤ 1,5, ou as tarefas de maior M15 não coincidem com as páginas não adaptadas em M14. A comparação de M5 e M6 só é feita se ao menos três participantes executarem as mesmas tarefas nos dois tipos de dispositivo |
| HR2 | Eficiência de Desempenho → Capacidade de Interação | As tarefas com maior tempo de carregamento são as de maior tempo relativo de execução. | Ordenação das seis tarefas por M16 por tarefa (condição de rede das sessões) e por M6, com correlação de postos de Spearman usada apenas de forma descritiva; a ordenação é repetida com M17 | Com seis tarefas, a correlação não terá significância estatística; se as ordenações divergirem, a relação é declarada não estabelecida |
| HR3 | Capacidade de Interação → Adequação Funcional | Ocorrem casos em que o participante afirma que uma função não existe, embora ela exista. | Métrica auxiliar MA1 ([Métricas](metricas.md#ma1-taxa-de-declaracao-de-funcao-inexistente)) | Nenhuma ocorrência registrada (MA1 = 0) |
| HR4 | Eficiência de Desempenho → Flexibilidade | O tempo de carregamento em rede móvel simulada é pelo menos o dobro do tempo em rede comum. | Razão M17 / M16, no geral e por página | Razão menor que 2,0, ou medições incompletas em uma das condições de rede |

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 17/10/2026 | Definição das hipóteses H1 a H9 | Felipe Campêlo |
| 2.0 | 18/10/2026 | Estrutura da página alinhada à Fase 1 reestruturada (H1 a H14), para preenchimento | Felipe Campêlo |
| 2.1 | 18/10/2026 | Preenchimento das hipóteses H1 a H14 a partir da versão complementar, com fundamento na Fase 1 e critério de confirmação numérico; critérios de classificação das hipóteses; hipóteses de relação HR1 a HR4 | Leonardo Bonetti |
