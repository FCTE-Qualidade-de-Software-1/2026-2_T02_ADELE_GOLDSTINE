# Fase 4 - Execução da Avaliação

<!-- Critérios F4: execução conforme o plano, dados rastreáveis, cálculo, julgamento e coerência com o propósito. -->

Esta fase corresponde à quarta atividade do processo de avaliação de produto da **ISO/IEC 25040** [1]: as medidas são obtidas conforme o plano da [Fase 3](../fase-3/index.md), comparadas aos [níveis de pontuação](../fase-2/niveis-pontuacao.md) e julgadas. Esta página acompanha a execução enquanto a coleta está em andamento; o julgamento final das três características é feito depois que todas as métricas forem calculadas, conforme o [cronograma](../fase-3/cronograma.md).

## Situação da coleta

*Tabela 1 - Situação da coleta por método em 22/11/2026.*

| Método | Métricas | Situação | Página |
| ------ | -------- | -------- | ------ |
| Teste com usuários e questionário | M3 a M8, M11, M12, MA1 | Concluída com 5 participantes (P1, P2, P3, P4 e P6): M3 (60,0%), M4 (73,3%), M5 (83,3%), M6 (4,39×), M7 (1,46×), M8 (81,25%), M11 (53,3%) e M12 (32,5) | [Teste com usuários (gráficos)](teste-usuarios.md) |
| Acessibilidade automática (WAVE) | M9 | Concluída: 13,17 erros/página (79 erros em 6 páginas, Insatisfatório) | [Acessibilidade Automática (M9)](acessibilidade.md) |
| Inspeção por pares | M1, M2, M10, M20 | Não iniciada | - |
| Execução instrumentada | M13, M14 | Concluída: M13 (24/24, Excelente) e M14 (0/12, Insatisfatório) | [Flexibilidade](flexibilidade.md) |
| Execução manual em celular | M15 | Concluída: 1,59 (110,2 s no celular para 69,1 s no computador, Regular) | [Julgamento da Avaliação](julgamento.md) |
| Dados complementares (fora do julgamento) | Rapidez, responsividade, estabilidade e fluidez | Concluída (46 de 48 execuções válidas) | [Desempenho (complementar)](desempenho.md) |

*Fonte: elaboração da equipe.*

## Julgamento

A comparação de cada métrica com os níveis de pontuação, as respostas às questões Q1 a Q16, a classificação das hipóteses, o julgamento das três características, o ranking das tarefas e a ligação com o propósito da Fase 1 estão em [Julgamento da Avaliação](julgamento.md). Capacidade de Interação: ___. Adequação Funcional: ___. Flexibilidade: atende parcialmente.

## Ação de Melhoria Técnica (Seção 3.2)

Com base nos piores resultados medidos (**M14 = 0/12**, **M12 = 32,5**, **M9 = 13,17 erros/página**, **M6 = 4,39×**, **M3 = 60,0%** e **IQ4 = 100%** com necessidade de *zoom* e botões pequenos no celular), a equipe desenvolveu o **[Protótipo Mobile-First de Alta Fidelidade](prototipo-mobile.md)** (`360 × 800 px`) com especificação técnica, matriz de rastreabilidade (`RM-01` a `RM-10`), comparativo visual e simulador interativo navegável para as tarefas T1 a T6.

## Referências

[1] ISO/IEC 25040:2024. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality evaluation framework*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 15/11/2026 | Criação da página da Fase 4 com a situação da coleta | [arthurlleite](https://github.com/arthurlleite) |
| 1.1 | 21/11/2026 | Atualização da situação de M13 (24/24, concluída com Edge e WebKit) e inclusão dos resultados de M9 (WAVE) | [Felipe Campêlo](https://github.com/felipeacampelo) |
| 1.2 | 21/11/2026 | Consolidação da conclusão do teste com usuários (P1 a P4 e P6) e inclusão do link para o Protótipo Mobile (Ação de Melhoria Técnica) | [Davi Nobre](https://github.com/Jagaima) |
| 1.3 | 22/11/2026 | Inclusão do link para o julgamento da avaliação | Leonardo Bonetti |
| 1.4 | 22/11/2026 | Situação de M15 (concluída, 1,59) | Leonardo Bonetti |
