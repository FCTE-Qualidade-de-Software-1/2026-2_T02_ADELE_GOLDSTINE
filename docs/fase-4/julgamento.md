# Julgamento da Avaliação

<!-- Critérios F4-C3 a F4-C5: comparação com os níveis de pontuação, respostas às questões e aos objetivos do GQM, coerência com o propósito da Fase 1 e julgamento final. -->

Esta página reúne os resultados de todas as métricas da Fase 4 e aplica a eles os [critérios de julgamento](../fase-2/niveis-pontuacao.md#criterios-de-julgamento) definidos na Fase 2 antes da coleta. Cada métrica recebe um nível, que é o nível da sua questão (Etapa 1), e cada hipótese é classificada como confirmada, refutada ou inconclusiva ([regra 6](../fase-2/niveis-pontuacao.md#regra-6-classificacao-das-hipoteses)). Os valores vêm de [`dados/consolidados/metricas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/consolidados/metricas.csv), e o detalhamento de cada método está nas páginas de [Acessibilidade Automática (M9)](acessibilidade.md), [Teste com usuários (gráficos)](teste-usuarios.md) e [Flexibilidade](flexibilidade.md).

## 1. Situação das métricas

O gráfico abaixo mostra onde caíram as oito métricas do teste com usuários e do questionário; os demais gráficos desse método estão em [Teste com usuários (gráficos)](teste-usuarios.md). A Tabela 1 traz todas as métricas da avaliação. As planilhas da inspeção estão em [`dados/brutos/inspecao/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/tree/main/dados/brutos/inspecao), com as colunas dos dois avaliadores e o resultado final.

[[GRAFICO_TU:painel-metricas]]

*Tabela 1 - Valor e nível de cada métrica.*

| Objetivo | Questão | Métrica | Valor | Nível | Método |
| -------- | :-----: | ------- | ----- | ----- | ------ |
| G1 | Q1 | M1 - Cobertura funcional | 77,8% (14 de 18 funções) | Regular (1) | Inspeção por pares |
| G1 | Q2 | M2 - Taxa de correção funcional | 97,0% (65 de 67 verificações), sem divergência em item crítico | Bom (2) | Inspeção por pares |
| G1 | Q3 | M3 - Uso de ferramentas externas | 60,0% (3 de 5 participantes) | Insatisfatório (0) | Questionário |
| G2 | Q4 | M4 - Acerto na primeira escolha de menu | 73,3% (22 de 30 tentativas) | Regular (1) | Teste com usuários |
| G2 | Q5 | M5 - Conclusão de tarefas sem ajuda | 83,3% (25 de 30 tentativas) | Bom (2) | Teste com usuários |
| G2 | Q6 | M6 - Tempo relativo de execução | 4,39 (média de 6 tarefas) | Insatisfatório (0) | Teste com usuários |
| G2 | Q7 | M7 - Desvio de caminho | 1,46 (média de 4 tarefas) | Regular (1) | Teste com usuários |
| G2 | Q8 | M8 - Recuperação de erros | 81,25% (13 de 16 erros) | Bom (2) | Teste com usuários |
| G2 | Q9 | M20 - Tratamento de cenários de erro | 83,3% (5 de 6 cenários) | Bom (2) | Inspeção por pares |
| G2 | Q10 | M9 - Erros automáticos de acessibilidade | 13,17 erros por página (79 em 6 páginas) | Insatisfatório (0) | WAVE |
| G2 | Q11 | M10 - Critérios manuais de acessibilidade | 54,2% (13 de 24 verificações) | Insatisfatório (0) | Inspeção por pares |
| G2 | Q12 | M11 - Interpretação correta sem legenda | 53,3% (8 de 15 respostas) | Regular (1) | Teste com usuários |
| G2 | Q13 | M12 - Pontuação SUS | 32,5 (5 questionários) | Insatisfatório (0) | Questionário SUS |
| G3 | Q14 | M13 - Compatibilidade entre navegadores | 100% (24 de 24 combinações) | Excelente (3) | Execução instrumentada |
| G3 | Q15 | M14 - Páginas adaptadas a telas pequenas | 0% (0 de 12 verificações) | Insatisfatório (0) | Execução instrumentada |
| G3 | Q16 | M15 - Tempo relativo no celular | 1,59 (110,2 s no celular para 69,1 s no computador) | Regular (1) | Execução manual no celular |

*Fonte: elaboração da equipe, a partir de `dados/consolidados/metricas.csv` e das faixas de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#faixas-por-metrica).*

As faixas de M3 foram descritas na Fase 2 para seis participantes; com os cinco participantes do teste, cada um vale 20 pontos percentuais, e três participantes (60%) ficam acima do limite de 50% do nível Insatisfatório.

## 2. Respostas às questões e classificação das hipóteses

A resposta textual de cada questão segue o nível da sua métrica ([Tabela 4 de Níveis de Pontuação](../fase-2/niveis-pontuacao.md#etapa-1-pontuacao-da-questao)): Excelente, "Sim, plenamente"; Bom, "Sim"; Regular, "Parcialmente, com dificuldade relevante"; Insatisfatório, "Não". O critério de confirmação de cada hipótese é o registrado em [Hipóteses](../fase-2/hipoteses.md).

### 2.1 G1 - Adequação Funcional

*Tabela 2 - Respostas às questões e hipóteses de G1.*

| Questão | Nível | Resposta | Hipótese e critério | Classificação |
| :-----: | ----- | -------- | ------------------- | ------------- |
| Q1 | Regular (1) | Parcialmente, com dificuldade relevante | H1: M1 ≥ 75% e < 90% (Regular) | **Confirmada** |
| Q2 | Bom (2) | Sim | H2: M2 = 100% (Excelente) | **Refutada**: M2 = 97,0% ficou abaixo do previsto, com duas divergências em datas do calendário |
| Q3 | Insatisfatório (0) | Não | H3: M3 > 25% e ≤ 50% (Regular) | **Refutada**: M3 = 60% ficou acima da faixa prevista |

*Fonte: elaboração da equipe.*

**Q1 (confirmada).** Das 18 funções da lista de referência, 14 existem no SIGAA. Todas as funções necessárias às tarefas T1 a T6 existem (100% em cada tarefa); as quatro ausentes vêm das ferramentas da comunidade (OP-07): ver o fluxo do curso marcando o que já foi cursado, planejar os semestres até a formatura, montar a grade de horários antes de escolher as turmas (o SIGAA só a mostra na tela de confirmação da matrícula) e simular o IRA. A pergunta aberta do questionário sobre funções ausentes (F4) não teve respostas.

**Q2 (refutada para pior).** As 44 menções da tela de notas coincidem com o histórico, assim como o IRA, a MP e as cargas horárias pendentes do portal e dos índices acadêmicos, que são os itens críticos, e os horários de três turmas no portal e na Turma Virtual. As duas divergências estão no calendário de T6: o SIGAA registra um dia para o processamento da matrícula (30/07) e da rematrícula (05/08), e o calendário publicado pela SAA registra dois (30 e 31/07; 05 e 06/08). Nenhuma afeta prazos que dependem do estudante.

**Q3.** As funções do SIGAA não bastam para que o estudante planeje o fluxo sem ferramentas externas: três dos cinco participantes usam uma ferramenta da comunidade ou uma planilha própria. H3 previa o uso por até metade dos participantes; o resultado foi pior que o esperado, o que reforça a observação OP-07 da Fase 1.

### 2.2 G2 - Capacidade de Interação

*Tabela 3 - Respostas às questões e hipóteses de G2.*

| Questão | Nível | Resposta | Hipótese e critério | Classificação |
| :-----: | ----- | -------- | ------------------- | ------------- |
| Q4 | Regular (1) | Parcialmente, com dificuldade relevante | H4: M4 ≥ 50% e < 75% (Regular) | **Confirmada** |
| Q5 | Bom (2) | Sim | H5: M5 ≥ 78% e < 90% (Bom) e, no recorte de calouros, M5 < 65% | **Refutada**: M5 = 83,3% está na faixa prevista, mas os calouros concluíram 83,3% das tarefas (10 de 12), o mesmo que o meio ou fim do curso, e 3 de 3 nas tarefas que nunca tinham feito, acima dos 65% previstos |
| Q6 | Insatisfatório (0) | Não | H6: M6 > 2,5 e ≤ 4,0 (Regular) | **Refutada**: M6 = 4,39 ficou acima da faixa prevista |
| Q7 | Regular (1) | Parcialmente, com dificuldade relevante | H7: M7 > 1,33 e ≤ 2,00 (Regular) | **Confirmada** |
| Q8 | Bom (2) | Sim | H8: M8 ≥ 50% e < 70% (Regular) | **Refutada**: M8 = 81,25% ficou acima da faixa prevista |
| Q9 | Bom (2) | Sim | H9: M20 < 50% (Insatisfatório) | **Refutada**: M20 = 83,3% ficou acima da faixa prevista |
| Q10 | Insatisfatório (0) | Não | H10: M9 > 5 erros por página (Insatisfatório) | **Confirmada** |
| Q11 | Insatisfatório (0) | Não | H11: M10 ≥ 75% e < 90% (Regular) | **Refutada**: M10 = 54,2% ficou abaixo da faixa prevista |
| Q12 | Regular (1) | Parcialmente, com dificuldade relevante | H12: M11 ≥ 50% e < 75% (Regular), com a pergunta de T2 abaixo de 50% | **Confirmada**: M11 = 53,3%, e a pergunta de T2 teve 40% de acertos |
| Q13 | Insatisfatório (0) | Não | H13: M12 ≥ 51 e < 68 (Regular) | **Refutada**: M12 = 32,5 ficou abaixo da faixa prevista |

*Fonte: elaboração da equipe.*

**Q4, Q7 e Q12 (confirmadas).** O estudante chega à função e entende o que vê, mas com dificuldade: erra o primeiro clique em cerca de uma a cada quatro tentativas, faz em média 1,46 vez os cliques do caminho mais curto e interpreta corretamente pouco mais da metade das informações sem a legenda. O código de horário de T2 foi a informação mais difícil (40% de acertos), como previa a observação OP-01.

**Q6 e Q13 (refutadas para pior).** O tempo e a satisfação ficaram abaixo do previsto. Os participantes levaram, em média, 4,39 vezes o tempo do especialista, com o pior caso em T4 (8,48 vezes), e nenhuma pontuação SUS individual alcançou o limite do nível Regular (entre 17,5 e 45,0). A Fase 1 tratava o SIGAA como "usável, porém trabalhoso"; os dados indicam que o esforço e a insatisfação são maiores que isso.

**Q5 e Q8 (resultados melhores que os de tempo e satisfação).** Os participantes concluíram sem ajuda 25 das 30 tentativas e se recuperaram sozinhos de 13 dos 16 erros. H8 previa recuperação entre 50% e 70%, porque erros como a expiração da sessão obrigariam a refazer passos. Nas sessões, 15 dos 16 erros foram escolhas de item errado, desfeitas pelo próprio participante ao voltar ao portal; o único erro do sistema, a página "Document Expired" depois do botão Voltar na Turma Virtual, obrigou a refazer passos. Os outros dois erros não recuperados vieram do link do calendário no painel do portal, que leva ao site da SAA (T6). As falhas de conclusão concentraram-se em T4 e T6 (60% de conclusão em cada uma). Os dois participantes do começo do curso concluíram tanto quanto os do meio ou fim (83,3% nos dois grupos) e todas as tarefas que faziam pela primeira vez: a falta de experiência não impediu a conclusão. A diferença entre os grupos aparece na satisfação, com SUS médio de 22,5 no começo do curso e 39,2 no meio ou fim. Esses resultados, lidos com Q6 e Q13, indicam que o estudante consegue terminar as tarefas, mas a um custo alto de tempo e de satisfação.

**Q9 (refutada para melhor).** O sistema tratou cinco dos seis cenários: o botão Voltar, a recarga da página e a segunda aba não geraram erro; a matrícula fora do período é bloqueada com mensagem e datas; e o atestado e o histórico abrem sem janela nova, de modo que o bloqueio de pop-ups não os afeta. O cenário não tratado é a sessão expirada (C1, OP-06): depois de 42 minutos parado, o clique em uma função levou de volta ao portal, sem abrir a função e sem mensagem sobre a sessão. A página "Document Expired" vista pelo P2 no teste com usuários não se reproduziu na inspeção, em Chromium, Firefox e WebKit.

**Q10 (confirmada).** As seis páginas têm, juntas, 79 erros automáticos de acessibilidade, com a maior concentração na Turma Virtual (T5, 37 erros) e no portal inicial (T2, 22 erros). O detalhamento está em [Acessibilidade Automática (M9)](acessibilidade.md).

**Q11 (refutada para pior).** Das 24 verificações manuais, 13 foram atendidas. O menu principal do portal (Ensino) não recebe o foco do teclado e é anunciado pelo leitor de tela só como "botão, conteúdo da web", sem o nome: por isso T1, T3, T4 e T6, que começam por ele, falham nos critérios de teclado (a) e de nome acessível (d). No portal (T2) e no calendário (T6), o foco passa por um quadro invisível e desaparece (critério b). Com zoom de 200%, só a Turma Virtual (T5) perde informação, com textos sobrepostos, o mesmo defeito do critério (c) de M14. A pior página é a do calendário (T6, 1 de 4).

### 2.3 G3 - Flexibilidade

*Tabela 4 - Respostas às questões e hipóteses de G3.*

| Questão | Nível | Resposta | Hipótese e critério | Classificação |
| :-----: | ----- | -------- | ------------------- | ------------- |
| Q14 | Excelente (3) | Sim, plenamente | H14: M13 ≥ 90% e < 100% (Bom) | **Refutada**: M13 = 100% ficou acima da faixa prevista |
| Q15 | Insatisfatório (0) | Não | H15: M14 < 50% (Insatisfatório) | **Confirmada** |
| Q16 | Regular (1) | Parcialmente, com dificuldade relevante | H16: M15 > 1,5 e ≤ 2,0 (Regular) | **Confirmada** |

*Fonte: elaboração da equipe, com as classificações de H14 e H15 registradas em [Flexibilidade](flexibilidade.md) e os tempos de M15 em [`dados/brutos/flexibilidade/tempos-celular.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/tempos-celular.csv).*

**Q14 e Q15.** No computador, as seis tarefas funcionaram nos quatro navegadores; no celular e no tablet, nenhuma das seis páginas se adapta à tela. As duas respostas confirmam o que a Fase 1 apontava (OP-02 e OP-03): o problema de Flexibilidade do SIGAA está na tela pequena e no toque, e não no navegador.

**Q16 (confirmada).** As seis tarefas levaram, no celular, 1,59 vez o tempo no computador, executadas pelo mesmo avaliador, pelo caminho mais curto e na mesma rede. A diferença se concentra nas tarefas em que é preciso ler tabelas pequenas ou tocar em vários alvos: T2 (2,03), T5 (1,96) e T6 (1,89). Nas tarefas que terminam em um PDF ou na leitura do painel inicial, o tempo foi parecido nos dois aparelhos: T3 (1,05) e T4 (1,09). O estudante consegue concluir as tarefas no celular, mas com esforço adicional, como previa H16.

### 2.4 Síntese das hipóteses

*Tabela 5 - Classificação das hipóteses H1 a H16.*

| Classificação | Hipóteses | Total |
| ------------- | --------- | :---: |
| Confirmada | H1, H4, H7, H10, H12, H15, H16 | 7 |
| Refutada | H2, H3, H5, H6, H8, H9, H11, H13, H14 | 9 |

*Fonte: elaboração da equipe.*

Entre as hipóteses refutadas, H5, H8, H9 e H14 erraram para melhor, e H2, H3, H6, H11 e H13, para pior. As refutações para pior concentram-se no esforço, na satisfação e na acessibilidade: as hipóteses da Fase 1 subestimaram o quanto o uso do SIGAA é demorado, insatisfatório e dependente do mouse. Em H2, a diferença é pequena (97,0% contra 100%) e não atinge item crítico.

## 3. Julgamento das características

A pontuação de cada objetivo é a média dos níveis das suas questões ([Etapa 2](../fase-2/niveis-pontuacao.md#etapa-2-pontuacao-do-objetivo)), e o julgamento segue a [Tabela 6 de Níveis de Pontuação](../fase-2/niveis-pontuacao.md#etapa-3-julgamento-da-caracteristica). As características aparecem na ordem de prioridade da Fase 1 ([regra 5](../fase-2/niveis-pontuacao.md#regra-5-ausencia-de-nota-unica)), e não há nota única para o SIGAA.

*Tabela 6 - Julgamento das características.*

| Objetivo | Níveis das questões | Média | Julgamento |
| -------- | ------------------- | :---: | ---------- |
| G2 - Capacidade de Interação | Q4 = 1, Q5 = 2, Q6 = 0, Q7 = 1, Q8 = 2, Q9 = 2, Q10 = 0, Q11 = 0, Q12 = 1, Q13 = 0 | 0,90 | **Não atende** |
| G1 - Adequação Funcional | Q1 = 1, Q2 = 2, Q3 = 0 | 1,00 | **Atende parcialmente** |
| G3 - Flexibilidade | Q14 = 3, Q15 = 0, Q16 = 1 | 1,33 | **Atende parcialmente** |

*Fonte: elaboração da equipe.*

**G2 - Capacidade de Interação: não atende.** A média é 0,90, abaixo de 1,0. Quatro questões são Insatisfatórias (tempo, acessibilidade automática, acessibilidade manual e satisfação). O estudante conclui a maior parte das tarefas e se recupera da maior parte dos erros (Q5 e Q8, Bom), mas leva mais de quatro vezes o tempo de um usuário experiente, encontra barreiras de acessibilidade em todas as páginas, não consegue usar o menu principal sem mouse e avalia o sistema na faixa mais baixa do SUS. O sistema trata bem a maior parte dos erros previsíveis (Q9, Bom), com exceção da sessão expirada.

**G1 - Adequação Funcional: atende parcialmente.** A média é 1,00, e a pertinência funcional (Q3) Insatisfatória impede o julgamento "Atende". O SIGAA tem todas as funções das tarefas do escopo e mostra as informações acadêmicas corretas (Q2, Bom, sem divergência em item crítico), mas não oferece o planejamento do fluxo que leva três em cada cinco participantes a ferramentas externas (Q1 e Q3).

**G3 - Flexibilidade: atende parcialmente.** Q15 Insatisfatória impede o julgamento "Atende", e a média é 1,33. O SIGAA é plenamente compatível com os navegadores de computador (Q14, Excelente), nada adaptado a telas pequenas e ao toque (Q15, Insatisfatório) e, no celular, exige cerca de 60% mais tempo para as mesmas tarefas (Q16, Regular). A média não representa um sistema "médio": ela soma um ponto forte e um ponto crítico, e a separação por questão mostra onde está o problema.

## 4. Hipóteses de relação entre as características

*Tabela 7 - Verificação das hipóteses de relação.*

| ID | Relação | Resultado | Situação |
| -- | ------- | --------- | -------- |
| HR1 | Flexibilidade → Capacidade de Interação | M15 = 1,59, acima do limite de 1,5 do critério de refutação. Nenhuma das seis páginas é adaptada (M14 = 0 de 12), e as maiores razões estão em T2 (2,03), T5 (1,96) e T6 (1,89); T5 é a única página que também falha no critério (c) de M14, com texto sobreposto. A comparação complementar de M5 e M6 entre computador e celular não se aplica: pelo [protocolo](../fase-3/teste-usuarios.md), todas as sessões do teste com usuários foram feitas em computador | **Estabelecida, com ressalva** |
| HR2 | Capacidade de Interação → Adequação Funcional | MA1 = 0: em nenhuma das 30 tentativas o participante afirmou que uma função existente não existia | **Não estabelecida** |

*Fonte: elaboração da equipe, com os critérios de [Hipóteses de relação](../fase-2/hipoteses.md#hipoteses-de-relacao-entre-as-caracteristicas).*

HR1 não foi refutada: o celular exige mais esforço, e as tarefas de maior razão estão em páginas não adaptadas. A ressalva é que M14 não distingue as páginas (todas falham), então o cruzamento não mostra se uma página adaptada teria razão menor; T3 e T4, também em páginas não adaptadas, tiveram razão próxima de 1 porque terminam em um PDF ou na leitura do painel, sem navegação em menus.

HR2 previa que a dificuldade de interação levaria o estudante a concluir que uma função não existe. Isso não ocorreu: quando não encontraram a função, os participantes desistiram ou concluíram a tarefa fora do SIGAA, como nos dois casos de T6 em que o link do painel levou ao site da SAA. A dificuldade de interação aparece no tempo, nos desvios e na satisfação, mas não se converteu em percepção de falta de função.

## 5. Ranking das tarefas

A [regra 4](../fase-2/niveis-pontuacao.md#regra-4-ranking-das-tarefas) ordena as tarefas pela média dos níveis de M5, M6, M7 e M1 calculados para cada uma, com as mesmas faixas da Tabela 1. M7 não se aplica a T2 e T4, cujo caminho mais curto é zero clique (a informação está na página inicial), e fica fora da média dessas tarefas (regra 1).

*Tabela 8 - Índice das tarefas pela regra 4.*

| Tarefa | M5 (conclusão sem ajuda) | M6 (tempo relativo) | M7 (desvio de caminho) | M1 | Índice | Posição |
| ------ | ------------------------ | ------------------- | ---------------------- | :-: | :----: | :-----: |
| T1 - Notas de uma disciplina | 100% - Excelente (3) | 4,50 - Insatisfatório (0) | 1,40 - Regular (1) | 100% - Excelente (3) | 1,75 | 3ª |
| T2 - Dia, horário e local de uma turma | 100% - Excelente (3) | 2,58 - Regular (1) | Não se aplica | 100% - Excelente (3) | 2,33 | 5ª |
| T3 - Atestado ou histórico | 100% - Excelente (3) | 3,78 - Regular (1) | 1,00 - Excelente (3) | 100% - Excelente (3) | 2,50 | 6ª |
| T4 - Índices e carga horária pendente | 60% - Regular (1) | 8,48 - Insatisfatório (0) | Não se aplica | 100% - Excelente (3) | 1,33 | 2ª |
| T5 - Material na Turma Virtual | 80% - Bom (2) | 2,32 - Bom (2) | 1,63 - Regular (1) | 100% - Excelente (3) | 2,00 | 4ª |
| T6 - Calendário acadêmico | 60% - Regular (1) | 4,67 - Insatisfatório (0) | 1,83 - Regular (1) | 100% - Excelente (3) | 1,25 | 1ª (pior) |

*Fonte: elaboração da equipe, a partir dos recortes por tarefa de `dados/consolidados/metricas.csv`.*

As tarefas de pior índice são T6 (1,25) e T4 (1,33). M1 é 100% em todas as tarefas e não diferencia o ranking, que fica determinado pelo comportamento dos participantes. T4 e T6 são as únicas com conclusão sem ajuda no nível Regular: dois em cada cinco participantes não as concluíram. Em T4, a informação está na página inicial, mas os participantes que a encontraram fizeram, em média, 5,67 cliques até ela e levaram 8,48 vezes o tempo do especialista. Em T6, o link do calendário no painel do portal leva ao site da SAA, na página de Pós-Graduação, o que explica dois dos três erros não recuperados do teste. Em T1, apesar da conclusão de 100%, o tempo dos participantes foi 4,5 vezes o do especialista.

## 6. Coerência com o propósito da avaliação

A Fase 1 definiu as decisões que a avaliação deve apoiar ([Propósito e Partes Interessadas, Tabela 1](../fase-1/proposito-stakeholders.md#13-como-os-resultados-serao-usados)). A Tabela 9 mostra o que os resultados indicam para cada uma.

*Tabela 9 - Decisões da Fase 1 e o que os resultados indicam.*

| Decisão a ser apoiada | Quem decide | Resultado que embasa a decisão | O que os resultados indicam |
| --------------------- | ----------- | ------------------------------ | --------------------------- |
| Quais telas e fluxos do portal do discente priorizar em um ciclo de melhoria | STI/UnB | Ranking das tarefas (Tabela 8) e julgamento de Capacidade de Interação e Adequação Funcional | Priorizar T6 e T4, as tarefas de pior índice. Capacidade de Interação: não atende, com tempo, satisfação e acessibilidade Insatisfatórios; o menu principal precisa funcionar pelo teclado e pelo leitor de tela. Adequação Funcional: atende parcialmente; as informações estão corretas, e a lacuna é o planejamento do fluxo do curso |
| Investir ou não em uma interface responsiva ou aplicativo móvel | STI/UnB | Julgamento de Flexibilidade cruzado com o perfil de acesso | Investir na interface responsiva. O SIGAA funciona nos quatro navegadores de computador (M13 = 100%), mas nenhuma página se adapta ao celular (M14 = 0%), e as tarefas levam 1,59 vez o tempo do computador (M15). Todos os cinco participantes usam o SIGAA no celular, e três o usam como dispositivo principal ou tanto quanto o computador (IQ4) |
| Quais procedimentos precisam de tutorial, aviso ou orientação adicional | DEG e coordenações | Tarefas com maior taxa de erro ou abandono e funções de difícil localização | Orientar sobre T4 e T6, as tarefas com menor conclusão sem ajuda (60%) e com dois em cada cinco participantes que já precisaram de ajuda nelas (IQ2). Em T6, o aviso mais direto é sobre o link do painel, que leva ao calendário da Pós-Graduação. Em T2, explicar o código de horário, interpretado corretamente por 40% dos participantes |
| Se há necessidade de otimizar páginas específicas | STI/UnB | Medidas de comportamento temporal e uso de recursos | Eficiência de Desempenho ficou fora da especificação, e esta decisão não recebe julgamento. Os [dados complementares](desempenho.md) apontam a Turma Virtual (T5) como a página mais pesada: cerca de 1,9 MB transferidos e 19 s de espera no celular em 4G |
| Qual ação de melhoria executar na Fase 4 | Equipe avaliadora | Problema de maior impacto entre os julgamentos | A característica de pior julgamento é Capacidade de Interação (não atende), e a tarefa de pior índice é T6 (regra 4). Em Flexibilidade, o problema de maior alcance é a ausência de adaptação ao celular, usado por todos os participantes. A ação executada é o [Protótipo Mobile-First](prototipo-mobile.md), que trata T6 (calendário no próprio SIGAA), T4 (carga horária pendente em destaque) e a adaptação ao celular |

*Fonte: elaboração da equipe.*

O julgamento responde ao propósito da avaliação, que é dar à STI e ao DEG evidências para priorizar melhorias no portal do discente. O SIGAA permite que o estudante conclua a maior parte das tarefas no computador, mas com tempo, desvios e insatisfação altos, barreiras de acessibilidade em todas as páginas e nenhuma adaptação ao celular. As prioridades que saem dos dados são as tarefas de integralização e de calendário, a acessibilidade das páginas e a interface responsiva.

## 7. Limitações

- **Amostra do teste com usuários.** A coleta terminou com cinco participantes (P1, P2, P3, P4 e P6), recrutados por conveniência na FCTE. O grupo do começo do curso teve dois participantes e o do meio ou fim, três.
- **M14 por emulação.** As larguras de 360 e 768 px foram verificadas por emulação no navegador, e não em celular real ([Flexibilidade](flexibilidade.md)).
- **Inspeção (M1, M2, M10 e M20) sem a equipe completa.** O primeiro avaliador foi um *script* ([`coleta/inspecao_coleta.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/coleta/inspecao_coleta.py)) executado na conta de um membro da equipe; o segundo avaliador repetiu manualmente os pontos decisivos (teclado e VoiceOver no Safari, histórico com bloqueio de pop-ups, funções da matrícula) e conferiu as evidências dos demais. Não houve divergência, e por isso não houve terceiro avaliador. O zoom de 200% de M10 foi reproduzido com a janela reduzida à metade (683 × 384 px CSS), e T5 usou uma turma de Sistemas Operacionais. A comparação com o PPC prevista na ficha de M2 não foi feita: M2 usa o histórico, os índices e o calendário publicado pela SAA, que cobrem todos os itens críticos.
- **M15 com um avaliador.** A ficha prevê a média entre avaliadores; M15 foi medida por um avaliador, em um celular (Samsung Galaxy S25 Ultra, Chrome) e uma execução por tarefa. Os tempos foram marcados pela fala do avaliador nas gravações ("começando" e "pronto"), com incerteza de cerca de 0,3 s por marcação; o valor só mudaria de nível com um erro de cerca de 6% no tempo total.

## Referências

[1] ISO/IEC 25040:2024. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality evaluation framework*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 21/11/2026 | Criação da página: nível das métricas, respostas às questões Q1 a Q16, classificação das hipóteses H1 a H16, julgamento de G1, G2 e G3, hipóteses de relação, ranking das tarefas e coerência com o propósito da Fase 1 | Leonardo Bonetti |
| 1.1 | 22/11/2026 | Resultado de M15: resposta a Q16, H16 confirmada, pontuação de G3, verificação de HR1 e limitação de um avaliador | Leonardo Bonetti |
| 1.2 | 22/11/2026 | Resultados da inspeção (M1, M2, M10 e M20): respostas a Q1, Q2, Q9 e Q11, classificação de H1, H2, H5, H9 e H11, julgamento de G1 e G2, ranking das tarefas, Tabela 9 e limitação da inspeção | Caio Borges |
| 1.3 | 23/11/2026 | H5 refutada pelo recorte dos calouros, sem número mínimo de participantes; resultado dos calouros em Q5 | Caio Borges |
