# Julgamento da Avaliação

<!-- Critérios F4-C3 a F4-C5: comparação com os níveis de pontuação, respostas às questões e aos objetivos do GQM, coerência com o propósito da Fase 1 e julgamento final. -->

Esta página reúne os resultados de todas as métricas da Fase 4 e aplica a eles os [critérios de julgamento](../fase-2/niveis-pontuacao.md#criterios-de-julgamento) definidos na Fase 2 antes da coleta. Cada métrica recebe um nível, que é o nível da sua questão (Etapa 1), e cada hipótese é classificada como confirmada, refutada ou inconclusiva ([regra 6](../fase-2/niveis-pontuacao.md#regra-6-classificacao-das-hipoteses)). Os valores vêm de [`dados/consolidados/metricas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/consolidados/metricas.csv), e o detalhamento de cada método está nas páginas de [Acessibilidade Automática (M9)](acessibilidade.md), [Teste com usuários (gráficos)](teste-usuarios.md) e [Flexibilidade](flexibilidade.md).

As métricas da inspeção por pares (M1, M2, M10 e M20) e da execução manual no celular (M15) ainda não têm dados. As questões dessas métricas aparecem como **sem dados** e ficam fora das médias ([regra 1](../fase-2/niveis-pontuacao.md#regra-1-metricas-nao-aplicaveis)); a página indica, em cada ponto, o que pode mudar quando esses dados forem integrados.

## 1. Situação das métricas

*Tabela 1 - Valor e nível de cada métrica em 21/11/2026.*

| Objetivo | Questão | Métrica | Valor | Nível | Método |
| -------- | :-----: | ------- | ----- | ----- | ------ |
| G1 | Q1 | M1 - Cobertura funcional | Sem dados | - | Inspeção por pares |
| G1 | Q2 | M2 - Taxa de correção funcional | Sem dados | - | Inspeção por pares |
| G1 | Q3 | M3 - Uso de ferramentas externas | 60,0% (3 de 5 participantes) | Insatisfatório (0) | Questionário |
| G2 | Q4 | M4 - Acerto na primeira escolha de menu | 73,3% (22 de 30 tentativas) | Regular (1) | Teste com usuários |
| G2 | Q5 | M5 - Conclusão de tarefas sem ajuda | 83,3% (25 de 30 tentativas) | Bom (2) | Teste com usuários |
| G2 | Q6 | M6 - Tempo relativo de execução | 4,39 (média de 6 tarefas) | Insatisfatório (0) | Teste com usuários |
| G2 | Q7 | M7 - Desvio de caminho | 1,46 (média de 4 tarefas) | Regular (1) | Teste com usuários |
| G2 | Q8 | M8 - Recuperação de erros | 81,3% (13 de 16 erros) | Bom (2) | Teste com usuários |
| G2 | Q9 | M20 - Tratamento de cenários de erro | Sem dados | - | Inspeção por pares |
| G2 | Q10 | M9 - Erros automáticos de acessibilidade | 13,17 erros por página (79 em 6 páginas) | Insatisfatório (0) | WAVE |
| G2 | Q11 | M10 - Critérios manuais de acessibilidade | Sem dados | - | Inspeção por pares |
| G2 | Q12 | M11 - Interpretação correta sem legenda | 53,3% (8 de 15 respostas) | Regular (1) | Teste com usuários |
| G2 | Q13 | M12 - Pontuação SUS | 32,5 (5 questionários) | Insatisfatório (0) | Questionário SUS |
| G3 | Q14 | M13 - Compatibilidade entre navegadores | 100% (24 de 24 combinações) | Excelente (3) | Execução instrumentada |
| G3 | Q15 | M14 - Páginas adaptadas a telas pequenas | 0% (0 de 12 verificações) | Insatisfatório (0) | Execução instrumentada |
| G3 | Q16 | M15 - Tempo relativo no celular | Sem dados | - | Execução manual no celular |

*Fonte: elaboração da equipe, a partir de `dados/consolidados/metricas.csv` e das faixas de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#faixas-por-metrica).*

Das 16 métricas, 11 têm valor e nível. As faixas de M3 foram descritas na Fase 2 para seis participantes; com os cinco participantes do teste, cada um vale 20 pontos percentuais, e três participantes (60%) ficam acima do limite de 50% do nível Insatisfatório.

## 2. Respostas às questões e classificação das hipóteses

A resposta textual de cada questão segue o nível da sua métrica ([Tabela 4 de Níveis de Pontuação](../fase-2/niveis-pontuacao.md#etapa-1-pontuacao-da-questao)): Excelente, "Sim, plenamente"; Bom, "Sim"; Regular, "Parcialmente, com dificuldade relevante"; Insatisfatório, "Não". O critério de confirmação de cada hipótese é o registrado em [Hipóteses](../fase-2/hipoteses.md).

### 2.1 G1 - Adequação Funcional

*Tabela 2 - Respostas às questões e hipóteses de G1.*

| Questão | Nível | Resposta | Hipótese e critério | Classificação |
| :-----: | ----- | -------- | ------------------- | ------------- |
| Q1 | Sem dados | - | H1: M1 ≥ 75% e < 90% (Regular) | Inconclusiva (M1 sem dados) |
| Q2 | Sem dados | - | H2: M2 = 100% (Excelente) | Inconclusiva (M2 sem dados) |
| Q3 | Insatisfatório (0) | Não | H3: M3 > 25% e ≤ 50% (Regular) | **Refutada**: M3 = 60% ficou acima da faixa prevista |

*Fonte: elaboração da equipe.*

**Q3.** As funções do SIGAA não bastam para que o estudante planeje o fluxo sem ferramentas externas: três dos cinco participantes usam uma ferramenta da comunidade ou uma planilha própria. H3 previa o uso por até metade dos participantes; o resultado foi pior que o esperado, o que reforça a observação OP-07 da Fase 1.

### 2.2 G2 - Capacidade de Interação

*Tabela 3 - Respostas às questões e hipóteses de G2.*

| Questão | Nível | Resposta | Hipótese e critério | Classificação |
| :-----: | ----- | -------- | ------------------- | ------------- |
| Q4 | Regular (1) | Parcialmente, com dificuldade relevante | H4: M4 ≥ 50% e < 75% (Regular) | **Confirmada** |
| Q5 | Bom (2) | Sim | H5: M5 ≥ 78% e < 90% (Bom) e, no recorte de calouros com ao menos três participantes, M5 < 65% | **Inconclusiva**: a primeira condição foi atendida, mas o grupo do começo do curso teve dois participantes, e o recorte fica sem nível (regra 3) |
| Q6 | Insatisfatório (0) | Não | H6: M6 > 2,5 e ≤ 4,0 (Regular) | **Refutada**: M6 = 4,39 ficou acima da faixa prevista |
| Q7 | Regular (1) | Parcialmente, com dificuldade relevante | H7: M7 > 1,33 e ≤ 2,00 (Regular) | **Confirmada** |
| Q8 | Bom (2) | Sim | H8: M8 ≥ 50% e < 70% (Regular) | **Refutada**: M8 = 81,3% ficou acima da faixa prevista |
| Q9 | Sem dados | - | H9: M20 < 50% (Insatisfatório) | Inconclusiva (M20 sem dados) |
| Q10 | Insatisfatório (0) | Não | H10: M9 > 5 erros por página (Insatisfatório) | **Confirmada** |
| Q11 | Sem dados | - | H11: M10 ≥ 75% e < 90% (Regular) | Inconclusiva (M10 sem dados) |
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
| Q16 | Sem dados | - | H16: M15 > 1,5 e ≤ 2,0 (Regular) | Inconclusiva (M15 sem dados) |

*Fonte: elaboração da equipe, com as classificações de H14 e H15 registradas em [Flexibilidade](flexibilidade.md).*

**Q14 e Q15.** No computador, as seis tarefas funcionaram nos quatro navegadores; no celular e no tablet, nenhuma das seis páginas se adapta à tela. As duas respostas confirmam o que a Fase 1 apontava (OP-02 e OP-03): o problema de Flexibilidade do SIGAA está na tela pequena e no toque, e não no navegador.

### 2.4 Síntese das hipóteses

*Tabela 5 - Classificação das hipóteses H1 a H16.*

| Classificação | Hipóteses | Total |
| ------------- | --------- | :---: |
| Confirmada | H4, H7, H10, H12, H15 | 5 |
| Refutada | H3, H6, H8, H13, H14 | 5 |
| Inconclusiva por falta de dados | H1, H2, H9, H11, H16 | 5 |
| Inconclusiva por recorte insuficiente | H5 | 1 |

*Fonte: elaboração da equipe.*

Das cinco hipóteses refutadas, duas erraram para melhor (H8 e H14) e três para pior (H3, H6 e H13). As refutações para pior estão todas na percepção e no esforço do estudante: as hipóteses da Fase 1 subestimaram o quanto o uso do SIGAA é demorado e insatisfatório.

## Referências

[1] ISO/IEC 25040:2024. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality evaluation framework*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 21/11/2026 | Situação das 16 métricas, respostas às questões e classificação das hipóteses H1 a H16 | Leonardo Bonetti |
