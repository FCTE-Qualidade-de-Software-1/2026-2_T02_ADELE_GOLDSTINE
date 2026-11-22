# Julgamento da Avaliação

<!-- Critérios F4-C3 a F4-C5: comparação com os níveis de pontuação, respostas às questões e aos objetivos do GQM, coerência com o propósito da Fase 1 e julgamento final. -->

Esta página reúne os resultados de todas as métricas da Fase 4 e aplica a eles os [critérios de julgamento](../fase-2/niveis-pontuacao.md#criterios-de-julgamento) definidos na Fase 2 antes da coleta. Cada métrica recebe um nível, que é o nível da sua questão (Etapa 1), e cada hipótese é classificada como confirmada, refutada ou inconclusiva ([regra 6](../fase-2/niveis-pontuacao.md#regra-6-classificacao-das-hipoteses)). Os valores vêm de [`dados/consolidados/metricas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/consolidados/metricas.csv), e o detalhamento de cada método está nas páginas de [Acessibilidade Automática (M9)](acessibilidade.md), [Teste com usuários (gráficos)](teste-usuarios.md) e [Flexibilidade](flexibilidade.md).

## 1. Situação das métricas

O gráfico abaixo mostra onde caíram as oito métricas do teste com usuários e do questionário; os demais gráficos desse método estão em [Teste com usuários (gráficos)](teste-usuarios.md). A Tabela 1 traz todas as métricas da avaliação.

[[GRAFICO_TU:painel-metricas]]

*Tabela 1 - Valor e nível de cada métrica.*

| Objetivo | Questão | Métrica | Valor | Nível | Método |
| -------- | :-----: | ------- | ----- | ----- | ------ |
| G1 | Q1 | M1 - Cobertura funcional | ___ | ___ | Inspeção por pares |
| G1 | Q2 | M2 - Taxa de correção funcional | ___ | ___ | Inspeção por pares |
| G1 | Q3 | M3 - Uso de ferramentas externas | 60,0% (3 de 5 participantes) | Insatisfatório (0) | Questionário |
| G2 | Q4 | M4 - Acerto na primeira escolha de menu | 73,3% (22 de 30 tentativas) | Regular (1) | Teste com usuários |
| G2 | Q5 | M5 - Conclusão de tarefas sem ajuda | 83,3% (25 de 30 tentativas) | Bom (2) | Teste com usuários |
| G2 | Q6 | M6 - Tempo relativo de execução | 4,39 (média de 6 tarefas) | Insatisfatório (0) | Teste com usuários |
| G2 | Q7 | M7 - Desvio de caminho | 1,46 (média de 4 tarefas) | Regular (1) | Teste com usuários |
| G2 | Q8 | M8 - Recuperação de erros | 81,25% (13 de 16 erros) | Bom (2) | Teste com usuários |
| G2 | Q9 | M20 - Tratamento de cenários de erro | ___ | ___ | Inspeção por pares |
| G2 | Q10 | M9 - Erros automáticos de acessibilidade | 13,17 erros por página (79 em 6 páginas) | Insatisfatório (0) | WAVE |
| G2 | Q11 | M10 - Critérios manuais de acessibilidade | ___ | ___ | Inspeção por pares |
| G2 | Q12 | M11 - Interpretação correta sem legenda | 53,3% (8 de 15 respostas) | Regular (1) | Teste com usuários |
| G2 | Q13 | M12 - Pontuação SUS | 32,5 (5 questionários) | Insatisfatório (0) | Questionário SUS |
| G3 | Q14 | M13 - Compatibilidade entre navegadores | 100% (24 de 24 combinações) | Excelente (3) | Execução instrumentada |
| G3 | Q15 | M14 - Páginas adaptadas a telas pequenas | 0% (0 de 12 verificações) | Insatisfatório (0) | Execução instrumentada |
| G3 | Q16 | M15 - Tempo relativo no celular | ___ | ___ | Execução manual no celular |

*Fonte: elaboração da equipe, a partir de `dados/consolidados/metricas.csv` e das faixas de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#faixas-por-metrica).*

As faixas de M3 foram descritas na Fase 2 para seis participantes; com os cinco participantes do teste, cada um vale 20 pontos percentuais, e três participantes (60%) ficam acima do limite de 50% do nível Insatisfatório.

## 2. Respostas às questões e classificação das hipóteses

A resposta textual de cada questão segue o nível da sua métrica ([Tabela 4 de Níveis de Pontuação](../fase-2/niveis-pontuacao.md#etapa-1-pontuacao-da-questao)): Excelente, "Sim, plenamente"; Bom, "Sim"; Regular, "Parcialmente, com dificuldade relevante"; Insatisfatório, "Não". O critério de confirmação de cada hipótese é o registrado em [Hipóteses](../fase-2/hipoteses.md).

### 2.1 G1 - Adequação Funcional

*Tabela 2 - Respostas às questões e hipóteses de G1.*

| Questão | Nível | Resposta | Hipótese e critério | Classificação |
| :-----: | ----- | -------- | ------------------- | ------------- |
| Q1 | ___ | ___ | H1: M1 ≥ 75% e < 90% (Regular) | ___ |
| Q2 | ___ | ___ | H2: M2 = 100% (Excelente) | ___ |
| Q3 | Insatisfatório (0) | Não | H3: M3 > 25% e ≤ 50% (Regular) | **Refutada**: M3 = 60% ficou acima da faixa prevista |

*Fonte: elaboração da equipe.*

**Q3.** As funções do SIGAA não bastam para que o estudante planeje o fluxo sem ferramentas externas: três dos cinco participantes usam uma ferramenta da comunidade ou uma planilha própria. H3 previa o uso por até metade dos participantes; o resultado foi pior que o esperado, o que reforça a observação OP-07 da Fase 1.

### 2.2 G2 - Capacidade de Interação

*Tabela 3 - Respostas às questões e hipóteses de G2.*

| Questão | Nível | Resposta | Hipótese e critério | Classificação |
| :-----: | ----- | -------- | ------------------- | ------------- |
| Q4 | Regular (1) | Parcialmente, com dificuldade relevante | H4: M4 ≥ 50% e < 75% (Regular) | **Confirmada** |
| Q5 | Bom (2) | Sim | H5: M5 ≥ 78% e < 90% (Bom) e, no recorte de calouros com ao menos três participantes, M5 < 65% | ___ |
| Q6 | Insatisfatório (0) | Não | H6: M6 > 2,5 e ≤ 4,0 (Regular) | **Refutada**: M6 = 4,39 ficou acima da faixa prevista |
| Q7 | Regular (1) | Parcialmente, com dificuldade relevante | H7: M7 > 1,33 e ≤ 2,00 (Regular) | **Confirmada** |
| Q8 | Bom (2) | Sim | H8: M8 ≥ 50% e < 70% (Regular) | **Refutada**: M8 = 81,25% ficou acima da faixa prevista |
| Q9 | ___ | ___ | H9: M20 < 50% (Insatisfatório) | ___ |
| Q10 | Insatisfatório (0) | Não | H10: M9 > 5 erros por página (Insatisfatório) | **Confirmada** |
| Q11 | ___ | ___ | H11: M10 ≥ 75% e < 90% (Regular) | ___ |
| Q12 | Regular (1) | Parcialmente, com dificuldade relevante | H12: M11 ≥ 50% e < 75% (Regular), com a pergunta de T2 abaixo de 50% | **Confirmada**: M11 = 53,3%, e a pergunta de T2 teve 40% de acertos |
| Q13 | Insatisfatório (0) | Não | H13: M12 ≥ 51 e < 68 (Regular) | **Refutada**: M12 = 32,5 ficou abaixo da faixa prevista |

*Fonte: elaboração da equipe.*

**Q4, Q7 e Q12 (confirmadas).** O estudante chega à função e entende o que vê, mas com dificuldade: erra o primeiro clique em cerca de uma a cada quatro tentativas, faz em média 1,46 vez os cliques do caminho mais curto e interpreta corretamente pouco mais da metade das informações sem a legenda. O código de horário de T2 foi a informação mais difícil (40% de acertos), como previa a observação OP-01.

**Q6 e Q13 (refutadas para pior).** O tempo e a satisfação ficaram abaixo do previsto. Os participantes levaram, em média, 4,39 vezes o tempo do especialista, com o pior caso em T4 (8,48 vezes), e nenhuma pontuação SUS individual alcançou o limite do nível Regular (entre 17,5 e 45,0). A Fase 1 tratava o SIGAA como "usável, porém trabalhoso"; os dados indicam que o esforço e a insatisfação são maiores que isso.

**Q5 e Q8 (resultados melhores que os de tempo e satisfação).** Os participantes concluíram sem ajuda 25 das 30 tentativas e se recuperaram sozinhos de 13 dos 16 erros. H8 previa recuperação entre 50% e 70%, porque erros como a expiração da sessão obrigariam a refazer passos. Nas sessões, 15 dos 16 erros foram escolhas de item errado, desfeitas pelo próprio participante ao voltar ao portal; o único erro do sistema, a página "Document Expired" depois do botão Voltar na Turma Virtual, obrigou a refazer passos. Os outros dois erros não recuperados vieram do link do calendário no painel do portal, que leva ao site da SAA (T6). As falhas de conclusão concentraram-se em T4 e T6 (60% de conclusão em cada uma). Esses resultados, lidos com Q6 e Q13, indicam que o estudante consegue terminar as tarefas, mas a um custo alto de tempo e de satisfação.

**Q10 (confirmada).** As seis páginas têm, juntas, 79 erros automáticos de acessibilidade, com a maior concentração na Turma Virtual (T5, 37 erros) e no portal inicial (T2, 22 erros). O detalhamento está em [Acessibilidade Automática (M9)](acessibilidade.md).

### 2.3 G3 - Flexibilidade

*Tabela 4 - Respostas às questões e hipóteses de G3.*

| Questão | Nível | Resposta | Hipótese e critério | Classificação |
| :-----: | ----- | -------- | ------------------- | ------------- |
| Q14 | Excelente (3) | Sim, plenamente | H14: M13 ≥ 90% e < 100% (Bom) | **Refutada**: M13 = 100% ficou acima da faixa prevista |
| Q15 | Insatisfatório (0) | Não | H15: M14 < 50% (Insatisfatório) | **Confirmada** |
| Q16 | ___ | ___ | H16: M15 > 1,5 e ≤ 2,0 (Regular) | ___ |

*Fonte: elaboração da equipe, com as classificações de H14 e H15 registradas em [Flexibilidade](flexibilidade.md).*

**Q14 e Q15.** No computador, as seis tarefas funcionaram nos quatro navegadores; no celular e no tablet, nenhuma das seis páginas se adapta à tela. As duas respostas confirmam o que a Fase 1 apontava (OP-02 e OP-03): o problema de Flexibilidade do SIGAA está na tela pequena e no toque, e não no navegador.

### 2.4 Síntese das hipóteses

*Tabela 5 - Classificação das hipóteses H1 a H16.*

| Classificação | Hipóteses | Total |
| ------------- | --------- | :---: |
| Confirmada | H4, H7, H10, H12, H15, ___ | ___ |
| Refutada | H3, H6, H8, H13, H14, ___ | ___ |
| Inconclusiva | ___ | ___ |

*Fonte: elaboração da equipe.*

Entre as hipóteses refutadas, H8 e H14 erraram para melhor, e H3, H6 e H13, para pior. As refutações para pior estão todas na percepção e no esforço do estudante: as hipóteses da Fase 1 subestimaram o quanto o uso do SIGAA é demorado e insatisfatório.

## 3. Julgamento das características

A pontuação de cada objetivo é a média dos níveis das suas questões ([Etapa 2](../fase-2/niveis-pontuacao.md#etapa-2-pontuacao-do-objetivo)), e o julgamento segue a [Tabela 6 de Níveis de Pontuação](../fase-2/niveis-pontuacao.md#etapa-3-julgamento-da-caracteristica). As características aparecem na ordem de prioridade da Fase 1 ([regra 5](../fase-2/niveis-pontuacao.md#regra-5-ausencia-de-nota-unica)), e não há nota única para o SIGAA.

*Tabela 6 - Julgamento das características.*

| Objetivo | Níveis das questões | Média | Julgamento |
| -------- | ------------------- | :---: | ---------- |
| G2 - Capacidade de Interação | Q4 = 1, Q5 = 2, Q6 = 0, Q7 = 1, Q8 = 2, Q9 = ___, Q10 = 0, Q11 = ___, Q12 = 1, Q13 = 0 | ___ | ___ |
| G1 - Adequação Funcional | Q1 = ___, Q2 = ___, Q3 = 0 | ___ | ___ |
| G3 - Flexibilidade | Q14 = 3, Q15 = 0, Q16 = ___ | ___ | **Atende parcialmente** |

*Fonte: elaboração da equipe.*

**G2 - Capacidade de Interação: ___.** Três questões são Insatisfatórias (tempo, acessibilidade automática e satisfação), o que impede o julgamento "Atende". O estudante conclui a maior parte das tarefas e se recupera da maior parte dos erros (Q5 e Q8, Bom), mas leva mais de quatro vezes o tempo de um usuário experiente, encontra barreiras de acessibilidade em todas as páginas e avalia o sistema na faixa mais baixa do SUS. ___

**G1 - Adequação Funcional: ___.** A pertinência funcional (Q3) é Insatisfatória, o que impede o julgamento "Atende". ___

**G3 - Flexibilidade: atende parcialmente.** Q15 Insatisfatória impede o julgamento "Atende", e, com Q14 Excelente, a média não fica abaixo de 1,0. O SIGAA é plenamente compatível com os navegadores de computador (Q14, Excelente) e nada adaptado a telas pequenas e ao toque (Q15, Insatisfatório). A média não representa um sistema "médio": ela soma um ponto forte e um ponto crítico, e a separação por questão mostra onde está o problema.

## 4. Hipóteses de relação entre as características

*Tabela 7 - Verificação das hipóteses de relação.*

| ID | Relação | Resultado | Situação |
| -- | ------- | --------- | -------- |
| HR1 | Flexibilidade → Capacidade de Interação | M15 por tarefa cruzado com M14: ___. A comparação complementar de M5 e M6 entre computador e celular não se aplica: pelo [protocolo](../fase-3/teste-usuarios.md), todas as sessões do teste com usuários foram feitas em computador | ___ |
| HR2 | Capacidade de Interação → Adequação Funcional | MA1 = 0: em nenhuma das 30 tentativas o participante afirmou que uma função existente não existia | **Não estabelecida** |

*Fonte: elaboração da equipe, com os critérios de [Hipóteses de relação](../fase-2/hipoteses.md#hipoteses-de-relacao-entre-as-caracteristicas).*

HR2 previa que a dificuldade de interação levaria o estudante a concluir que uma função não existe. Isso não ocorreu: quando não encontraram a função, os participantes desistiram ou concluíram a tarefa fora do SIGAA, como nos dois casos de T6 em que o link do painel levou ao site da SAA. A dificuldade de interação aparece no tempo, nos desvios e na satisfação, mas não se converteu em percepção de falta de função.

## 5. Ranking das tarefas

A [regra 4](../fase-2/niveis-pontuacao.md#regra-4-ranking-das-tarefas) ordena as tarefas pela média dos níveis de M5, M6, M7 e M1 calculados para cada uma, com as mesmas faixas da Tabela 1. M7 não se aplica a T2 e T4, cujo caminho mais curto é zero clique (a informação está na página inicial), e fica fora da média dessas tarefas (regra 1).

*Tabela 8 - Índice das tarefas pela regra 4.*

| Tarefa | M5 (conclusão sem ajuda) | M6 (tempo relativo) | M7 (desvio de caminho) | M1 | Índice | Posição |
| ------ | ------------------------ | ------------------- | ---------------------- | :-: | :----: | :-----: |
| T1 - Notas de uma disciplina | 100% - Excelente (3) | 4,50 - Insatisfatório (0) | 1,40 - Regular (1) | ___ | ___ | ___ |
| T2 - Dia, horário e local de uma turma | 100% - Excelente (3) | 2,58 - Regular (1) | Não se aplica | ___ | ___ | ___ |
| T3 - Atestado ou histórico | 100% - Excelente (3) | 3,78 - Regular (1) | 1,00 - Excelente (3) | ___ | ___ | ___ |
| T4 - Índices e carga horária pendente | 60% - Regular (1) | 8,48 - Insatisfatório (0) | Não se aplica | ___ | ___ | ___ |
| T5 - Material na Turma Virtual | 80% - Bom (2) | 2,32 - Bom (2) | 1,63 - Regular (1) | ___ | ___ | ___ |
| T6 - Calendário acadêmico | 60% - Regular (1) | 4,67 - Insatisfatório (0) | 1,83 - Regular (1) | ___ | ___ | ___ |

*Fonte: elaboração da equipe, a partir dos recortes por tarefa de `dados/consolidados/metricas.csv`.*

As tarefas de pior índice são ___. T4 e T6 são as únicas com conclusão sem ajuda no nível Regular: dois em cada cinco participantes não as concluíram. Em T4, a informação está na página inicial, mas os participantes que a encontraram fizeram, em média, 5,67 cliques até ela e levaram 8,48 vezes o tempo do especialista. Em T6, o link do calendário no painel do portal leva ao site da SAA, na página de Pós-Graduação, o que explica dois dos três erros não recuperados do teste. Em T1, apesar da conclusão de 100%, o tempo dos participantes foi 4,5 vezes o do especialista.

## 6. Coerência com o propósito da avaliação

A Fase 1 definiu as decisões que a avaliação deve apoiar ([Propósito e Partes Interessadas, Tabela 1](../fase-1/proposito-stakeholders.md#13-como-os-resultados-serao-usados)). A Tabela 9 mostra o que os resultados indicam para cada uma.

*Tabela 9 - Decisões da Fase 1 e o que os resultados indicam.*

| Decisão a ser apoiada | Quem decide | Resultado que embasa a decisão | O que os resultados indicam |
| --------------------- | ----------- | ------------------------------ | --------------------------- |
| Quais telas e fluxos do portal do discente priorizar em um ciclo de melhoria | STI/UnB | Ranking das tarefas (Tabela 8) e julgamento de Capacidade de Interação e Adequação Funcional | Priorizar ___, as tarefas de pior índice. Capacidade de Interação: ___. Adequação Funcional: ___ |
| Investir ou não em uma interface responsiva ou aplicativo móvel | STI/UnB | Julgamento de Flexibilidade cruzado com o perfil de acesso | Investir na interface responsiva. O SIGAA funciona nos quatro navegadores de computador (M13 = 100%), mas nenhuma página se adapta ao celular (M14 = 0%). Todos os cinco participantes usam o SIGAA no celular, e três o usam como dispositivo principal ou tanto quanto o computador (IQ4) |
| Quais procedimentos precisam de tutorial, aviso ou orientação adicional | DEG e coordenações | Tarefas com maior taxa de erro ou abandono e funções de difícil localização | Orientar sobre T4 e T6, as tarefas com menor conclusão sem ajuda (60%) e com dois em cada cinco participantes que já precisaram de ajuda nelas (IQ2). Em T6, o aviso mais direto é sobre o link do painel, que leva ao calendário da Pós-Graduação. Em T2, explicar o código de horário, interpretado corretamente por 40% dos participantes |
| Se há necessidade de otimizar páginas específicas | STI/UnB | Medidas de comportamento temporal e uso de recursos | Eficiência de Desempenho ficou fora da especificação, e esta decisão não recebe julgamento. Os [dados complementares](desempenho.md) apontam a Turma Virtual (T5) como a página mais pesada: cerca de 1,9 MB transferidos e 19 s de espera no celular em 4G |
| Qual ação de melhoria executar na Fase 4 | Equipe avaliadora | Problema de maior impacto entre os julgamentos | A característica de pior julgamento é ___, e a tarefa de pior índice é ___ (regra 4). Em Flexibilidade, o problema de maior alcance é a ausência de adaptação ao celular, usado por todos os participantes |

*Fonte: elaboração da equipe.*

O julgamento responde ao propósito da avaliação, que é dar à STI e ao DEG evidências para priorizar melhorias no portal do discente. O SIGAA permite que o estudante conclua a maior parte das tarefas no computador, mas com tempo, desvios e insatisfação altos, barreiras de acessibilidade em todas as páginas e nenhuma adaptação ao celular. As prioridades que saem dos dados são as tarefas de integralização e de calendário, a acessibilidade das páginas e a interface responsiva.

## 7. Limitações

- **Amostra do teste com usuários.** A coleta terminou com cinco participantes (P1, P2, P3, P4 e P6), recrutados por conveniência na FCTE. O grupo do começo do curso teve dois participantes, e os recortes desse grupo são apenas descritivos (regra 3).
- **M14 por emulação.** As larguras de 360 e 768 px foram verificadas por emulação no navegador, e não em celular real ([Flexibilidade](flexibilidade.md)).

## Referências

[1] ISO/IEC 25040:2024. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality evaluation framework*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 21/11/2026 | Criação da página: nível das métricas, respostas às questões Q1 a Q16, classificação das hipóteses H1 a H16, julgamento de G1, G2 e G3, hipóteses de relação, ranking das tarefas e coerência com o propósito da Fase 1 | Leonardo Bonetti |
