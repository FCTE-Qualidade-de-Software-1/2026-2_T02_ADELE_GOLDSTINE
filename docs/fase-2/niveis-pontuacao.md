# Níveis de Pontuação e Critérios de Julgamento

Esta página define como os valores medidos (M1 a M15 e M20, página [Métricas](metricas.md)) serão julgados na Fase 4: a escala de níveis, as faixas de cada métrica e os critérios para combinar as métricas por questão e por objetivo (G1 a G3). Os limites foram definidos **antes da coleta** e não serão alterados após a obtenção dos dados, para que o julgamento não seja ajustado aos resultados.

## Escala de níveis

Todas as métricas com nível de pontuação usam a mesma escala ordinal de quatro níveis (Tabela 1), o que permite comparar e agregar resultados de métricas com unidades diferentes.

*Tabela 1 - Escala de níveis de pontuação.*

| Nível | Pontos | Significado |
| ----- | :----: | ----------- |
| Excelente | 3 | Supera o esperado; nenhuma ação necessária |
| Bom | 2 | Nível esperado de um sistema institucional adequado ao seu público |
| Regular | 1 | O estudante consegue realizar as tarefas, mas com dificuldade relevante; há oportunidade clara de melhoria |
| Insatisfatório | 0 | O atributo impede ou compromete seriamente as tarefas do estudante; exige ação corretiva prioritária |

**Regra de fronteira:** um valor exatamente igual ao limite entre dois níveis pertence ao nível superior (o de mais pontos). Nas métricas em que valores maiores são melhores, isso aparece como "≥"; nas métricas em que valores menores são melhores, como "≤". Exemplo: M5 = 78% está no nível Bom, e M6 = 2,5 também está no nível Bom.

Quando existe referência externa reconhecida, ela foi usada para definir os limites; nos demais casos, os limites foram definidos pela equipe, e a justificativa está registrada na coluna "Origem das faixas" das Tabelas 2 e 3.

## Faixas por métrica

### Métricas em que valores maiores são melhores

*Tabela 2 - Faixas das métricas em que valores maiores são melhores.*

| Métrica | Excelente | Bom | Regular | Insatisfatório | Origem das faixas |
| ------- | --------- | --- | ------- | -------------- | ----------------- |
| M1 - Cobertura funcional | 100% | 90% a < 100% | 75% a < 90% | < 75% | Definidas pela equipe: o SIGAA não tem alternativa institucional, e a ausência de mais de um quarto das funções necessárias é inaceitável |
| M2 - Taxa de correção funcional | 100% | 97% a < 100%, sem divergência em item crítico | 90% a < 97%, sem divergência em item crítico | < 90% ou qualquer divergência em item crítico | Definidas pela equipe: dados acadêmicos incorretos afetam decisões, por isso a escala é estreita e uma divergência em menção, IRA ou carga horária pendente leva direto a Insatisfatório (regra 2) |
| M4 - Acerto na primeira escolha de menu | ≥ 90% | 75% a < 90% | 50% a < 75% | < 50% | Definidas pela equipe: abaixo de 50%, o estudante erra o ponto de partida na maioria das tentativas |
| M5 - Taxa de conclusão de tarefas sem ajuda | ≥ 90% | 78% a < 90% | 60% a < 78% | < 60% | O limite do Bom parte da taxa média de conclusão de tarefas de 78% relatada por Sauro [1]; os demais limites foram definidos pela equipe |
| M8 - Taxa de recuperação de erros | ≥ 90% | 70% a < 90% | 50% a < 70% | < 50% | Definidas pela equipe: abaixo de 50%, a maior parte dos erros exige ajuda externa ou retrabalho |
| M10 - Critérios manuais de acessibilidade atendidos | 100% | 90% a < 100% | 75% a < 90% | < 75% | A WCAG 2.2 [2] exige atendimento integral, por isso o Excelente corresponde à conformidade em todas as verificações; os demais limites foram definidos pela equipe. Com 24 verificações: 24 (Excelente), 22 ou 23 (Bom), 18 a 21 (Regular), 17 ou menos (Insatisfatório) |
| M11 - Interpretação correta sem legenda | ≥ 90% | 75% a < 90% | 50% a < 75% | < 50% | Definidas pela equipe: abaixo de 50%, a informação é mal interpretada pela maioria e depende da legenda |
| M12 - Pontuação SUS | ≥ 80,3 | 68 a < 80,3 | 51 a < 68 | < 51 | Sauro e Lewis [3]: 68 é a média dos estudos com o SUS; a partir de 80,3, o resultado fica entre os melhores da escala de notas; abaixo de 51, na faixa mais baixa |
| M13 - Compatibilidade entre navegadores | 100% | 90% a < 100% | 75% a < 90% | < 75% | Definidas pela equipe: abaixo de 75%, ao menos um navegador inteiro deixa de concluir a maioria das tarefas. Com 24 combinações: 24, 22 ou 23, 18 a 21, 17 ou menos |
| M14 - Páginas adaptadas a telas pequenas e ao toque | 100% | 80% a < 100% | 50% a < 80% | < 50% | O critério 1.4.10 da WCAG 2.2 [2] pede exibição sem rolagem em duas dimensões; abaixo de 50%, o sistema não é adaptado a dispositivos móveis. Os demais limites foram definidos pela equipe. Com 12 verificações: 12, 10 ou 11, 6 a 9, 5 ou menos |
| M20 - Cobertura de tratamento de cenários de erro | 100% | 75% a < 100% | 50% a < 75% | < 50% | Definidas pela equipe. Com seis cenários: 6 tratados (Excelente), 5 (Bom), 3 ou 4 (Regular), 0 a 2 (Insatisfatório) |

### Métricas em que valores menores são melhores

*Tabela 3 - Faixas das métricas em que valores menores são melhores.*

| Métrica | Excelente | Bom | Regular | Insatisfatório | Origem das faixas |
| ------- | --------- | --- | ------- | -------------- | ----------------- |
| M3 - Uso de ferramentas externas | ≤ 10% | > 10% a 25% | > 25% a 50% | > 50% | Definidas pela equipe: até um em cada dez respondentes é compatível com preferências individuais; acima da metade, recorrer a ferramenta externa é a prática dominante |
| M6 - Tempo relativo de execução | ≤ 1,5 | > 1,5 a 2,5 | > 2,5 a 4,0 | > 4,0 | Definidas pela equipe: até 1,5 vez o tempo de um usuário experiente é considerado excelente para um usuário comum |
| M7 - Desvio de caminho | ≤ 1,11 | > 1,11 a 1,33 | > 1,33 a 2,00 | > 2,00 | Definidas pela equipe como o inverso da eficiência do caminho (caminho mais curto / realizado) de 0,90, 0,75 e 0,50: acima de 2,00, o participante faz mais que o dobro dos cliques necessários |
| M9 - Erros automáticos de acessibilidade por página | 0 | > 0 a 2 | > 2 a 5 | > 5 | Definidas pela equipe: a WCAG 2.2 [2] não admite erros, por isso só a ausência de erros é Excelente; como a ferramenta detecta apenas parte dos problemas, mais de cinco erros por página indica barreiras generalizadas |
| M15 - Tempo relativo no celular | ≤ 1,2 | > 1,2 a 1,5 | > 1,5 a 2,0 | > 2,0 | Definidas pela equipe: até 20% a mais de tempo no celular é atribuível à tela menor; acima do dobro, o celular não é alternativa prática ao computador |

A métrica auxiliar MA1 não recebe nível de pontuação, porque serve apenas para verificar a hipótese de relação HR2 ([Hipóteses](hipoteses.md#hipoteses-de-relacao-entre-as-caracteristicas)).

## Critérios de julgamento

O julgamento é feito sempre do nível quantitativo para o conceitual: primeiro cada métrica recebe um nível, depois cada questão e, por fim, cada objetivo.

### Etapa 1 - Pontuação da questão

O valor de cada métrica é comparado às faixas das Tabelas 2 e 3 e recebe um nível de 0 a 3. O nível de uma questão é o **menor nível entre as suas métricas** aplicáveis. A regra é conservadora: um atributo só é considerado Bom se todas as medidas que o descrevem estiverem no nível Bom ou acima. Exemplo: em Q6, se M6 = Bom e M7 = Regular, Q6 recebe Regular.

A resposta textual à questão segue o nível obtido (Tabela 4).

*Tabela 4 - Resposta à questão conforme o nível.*

| Nível da questão | Resposta à questão |
| ---------------- | ------------------ |
| Excelente (3) | Sim, plenamente |
| Bom (2) | Sim |
| Regular (1) | Parcialmente, com dificuldade relevante |
| Insatisfatório (0) | Não |

Na mesma etapa, a hipótese da questão é classificada como confirmada, refutada ou inconclusiva (regra 6).

### Etapa 2 - Pontuação do objetivo

A pontuação do objetivo é a **média dos níveis das suas questões** (Tabela 5). Usar as questões, e não as métricas, evita que uma subcaracterística com mais métricas pese mais que as outras. Questões sem dados suficientes ficam fora da média (regra 1).

*Tabela 5 - Questões combinadas em cada objetivo.*

| Objetivo | Questões combinadas |
| -------- | ------------------- |
| G1 - Adequação Funcional | Q1, Q2, Q3 |
| G2 - Capacidade de Interação (Usabilidade) | Q4, Q5, Q6, Q7, Q8, Q9, Q10 |
| G3 - Flexibilidade (Portabilidade) | Q11, Q12 |

### Etapa 3 - Julgamento da característica

A pontuação do objetivo determina o julgamento da característica correspondente (Tabela 6). As condições são verificadas de cima para baixo, e vale a primeira satisfeita.

*Tabela 6 - Julgamento da característica de qualidade.*

| Pontuação do objetivo | Julgamento da característica |
| :-------------------: | ---------------------------- |
| Média ≥ 2,5 e nenhuma questão abaixo de Bom | Atende plenamente |
| Média ≥ 2,0 e nenhuma questão Insatisfatória | Atende |
| Média ≥ 1,0, sem satisfazer as condições anteriores | Atende parcialmente |
| Média < 1,0 | Não atende |
| Mais da metade das questões sem dados suficientes | Inconclusivo |

Uma questão Insatisfatória impede o julgamento "Atende", mesmo com média alta: um problema grave em uma subcaracterística não é compensado por bons resultados nas demais. A condição "Inconclusivo" é verificada antes das outras.

### Regras complementares

#### Regra 1 - Métricas não aplicáveis

Uma métrica sem dados suficientes é registrada como **não aplicável** e fica fora do cálculo da questão. Exemplo: M6 e M7 de uma tarefa que nenhum participante concluiu (registradas à parte, conforme as fichas). Uma questão sem nenhuma métrica aplicável fica **sem dados** e fora da Etapa 2, e sua hipótese é classificada como inconclusiva. Em M8, a ausência de erros não torna a métrica não aplicável: a ficha define X = 1 quando B = 0.

#### Regra 2 - Itens críticos de M2

Menção, IRA e carga horária pendente são itens críticos. Qualquer divergência em item crítico leva M2 ao nível Insatisfatório, qualquer que seja o valor de X, porque compromete decisões de matrícula e de formatura.

#### Regra 3 - Resultados por perfil, por página e por tarefa

Além do valor geral, que é o único usado nas Etapas 1 a 3, os resultados são apresentados por perfil (calouro, veterano e formando, em M5, M6, M7 e M11), por página (M9, M10 e M14) e por tarefa, com as mesmas faixas das Tabelas 2 e 3. Esses recortes localizam os problemas, mas não alteram o nível da questão. Um recorte com menos de três participantes é apresentado apenas de forma descritiva, sem nível.

#### Regra 4 - Ranking das tarefas

Para apoiar a decisão da STI sobre quais telas e fluxos priorizar ([Fase 1](../fase-1/proposito-stakeholders.md#13-como-os-resultados-serao-usados)), cada tarefa recebe um índice:

> **Índice da tarefa** = média dos níveis de M5, M6, M7 e M1 calculados para aquela tarefa.

M1 por tarefa considera apenas as funções da lista de referência associadas àquela tarefa; métricas não aplicáveis na tarefa ficam fora da média (regra 1). As tarefas são ordenadas do menor índice (pior) para o maior. Em caso de empate, fica pior a tarefa com menor M5. A tarefa de pior índice, combinada com a característica de pior julgamento, orienta a escolha da ação de melhoria da Fase 4.

#### Regra 5 - Ausência de nota única

**Não será calculada uma nota única para o SIGAA.** As três características avaliadas medem aspectos diferentes, e uma média geral esconderia exatamente os problemas que a STI precisa priorizar. O resultado final é o quadro com o julgamento de cada característica, apresentado na ordem de prioridade da Fase 1 (Capacidade de Interação, Adequação Funcional e Flexibilidade), acompanhado do ranking das tarefas (regra 4).

#### Regra 6 - Classificação das hipóteses

Cada hipótese é classificada como confirmada, refutada ou inconclusiva comparando os valores obtidos com o critério de confirmação registrado em [Hipóteses](hipoteses.md#como-as-hipoteses-sao-formuladas-e-classificadas). A classificação não altera o nível das métricas nem o julgamento das características.

## Exemplo de aplicação

O exemplo abaixo usa **valores fictícios**, apenas para mostrar como um resultado é transformado em julgamento. Não são resultados da avaliação.

*Tabela 7 - Exemplo ilustrativo de julgamento de G3 (valores fictícios).*

| Métrica | Valor fictício | Nível | Questão | Nível da questão |
| ------- | :------------: | ----- | :-----: | ---------------- |
| M13 - Compatibilidade entre navegadores | 23 de 24 (95,8%) | Bom (2) | Q11 | Bom (2) |
| M14 - Páginas adaptadas a telas pequenas e ao toque | 7 de 12 (58,3%) | Regular (1) | Q12 | Regular (1), menor entre M14 e M15 |
| M15 - Tempo relativo no celular | 1,8 | Regular (1) | | |

Pontuação de G3 = (2 + 1) / 2 = 1,5. Não há questão Insatisfatória, mas a média é menor que 2,0. **Julgamento: Atende parcialmente.** Neste exemplo, H11 seria confirmada (esperava-se M13 Bom) e H12 seria refutada (esperava-se M14 Insatisfatório, e o valor fictício ficou em Regular).

## Referências

[1] SAURO, J. What is a good task-completion rate? *MeasuringU*, 2011.

[2] W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>. Acesso em: 18 out. 2026.

[3] SAURO, J.; LEWIS, J. R. *Quantifying the User Experience: Practical Statistics for User Research*. 2. ed. Morgan Kaufmann, 2016.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 17/10/2026 | Definição dos níveis de pontuação e dos critérios de julgamento | Felipe Campêlo |
| 2.0 | 18/10/2026 | Estrutura da página alinhada à Fase 1 reestruturada (M1 a M19, G1 a G4), para preenchimento | Felipe Campêlo |
| 2.1 | 18/10/2026 | Preenchimento a partir da versão complementar: escala com regra de fronteira, faixas de M1 a M20 com origem, Etapas 1 a 3, regras complementares (métricas não aplicáveis, itens críticos de M2, recortes, ranking das tarefas, ausência de nota única, classificação das hipóteses) e exemplo de aplicação em G4 | Leonardo Bonetti |
| 2.2 | 25/10/2026 | Remoção das faixas de M16 a M19 e do objetivo G4 (Eficiência de Desempenho); exemplo de aplicação refeito em G3; MA1 ligada à HR2 (antiga HR3) | Leonardo Bonetti |
