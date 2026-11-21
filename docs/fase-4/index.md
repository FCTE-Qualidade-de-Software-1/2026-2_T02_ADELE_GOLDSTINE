# Fase 4 - Execução da Avaliação

<!-- Critérios F4: execução conforme o plano, dados rastreáveis, cálculo, julgamento e coerência com o propósito. -->

Esta fase corresponde à quarta atividade do processo de avaliação de produto da **ISO/IEC 25040** [1]: as medidas são obtidas conforme o plano da [Fase 3](../fase-3/index.md), comparadas aos [níveis de pontuação](../fase-2/niveis-pontuacao.md) e julgadas. Esta página acompanha a execução enquanto a coleta está em andamento; o julgamento final das três características é feito depois que todas as métricas forem calculadas, conforme o [cronograma](../fase-3/cronograma.md).

## Situação da coleta

*Tabela 1 - Situação da coleta por método em 21/11/2026.*

| Método | Métricas | Situação | Página |
| ------ | -------- | -------- | ------ |
| Teste com usuários e questionário | M3 a M8, M11, M12, MA1 | 2 de 6 sessões integradas na `main` (P1 e P3); P2, P4 e P6 em revisão no PR #20 | Dados em `dados/brutos/testes-usuarios/` e `dados/brutos/questionario/` |
| Acessibilidade automática (WAVE) | M9 | Concluída: 13,17 erros/página (79 erros em 6 páginas, Insatisfatório) | [Acessibilidade Automática (M9)](acessibilidade.md) |
| Inspeção por pares | M1, M2, M10, M20 | Não iniciada | - |
| Execução instrumentada | M13, M14 | Concluída: M13 (24/24, Excelente) e M14 (0/12, Insatisfatório) | [Flexibilidade](flexibilidade.md) |
| Execução manual em celular | M15 | Não iniciada | - |
| Dados complementares (fora do julgamento) | Rapidez, responsividade, estabilidade e fluidez | Concluída (46 de 48 execuções válidas) | [Desempenho (complementar)](desempenho.md) |

*Fonte: elaboração da equipe.*

## Referências

[1] ISO/IEC 25040:2024. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality evaluation framework*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 15/11/2026 | Criação da página da Fase 4 com a situação da coleta | [arthurlleite](https://github.com/arthurlleite) |
| 1.1 | 21/11/2026 | Atualização da situação de M13 (24/24, concluída com Edge e WebKit) e inclusão dos resultados de M9 (WAVE) | [Felipe Campêlo](https://github.com/felipeacampelo) |
