# Teste com usuários: resultados em gráficos

<!-- Critérios F4-C2 e F4-C3: dados processados e apresentados com gráficos, com ligação direta ao dado bruto. -->

Esta página mostra, em gráficos, os resultados das cinco sessões do [teste com usuários](../fase-3/teste-usuarios.md) (P1, P2, P3, P4 e P6, em 15 e 16/11/2026) e do questionário aplicado ao fim de cada sessão. Cada gráfico responde a uma pergunta e tem, logo abaixo, a tabela com os dados que o geraram.

Os gráficos são gerados no build do site por `coleta/graficos_testes.py`, a partir dos mesmos arquivos usados no cálculo das métricas (`coleta/calcular_testes.py`): `dados/brutos/testes-usuarios/`, `dados/brutos/questionario/`, `dados/referencia/` e `dados/consolidados/metricas.csv`. Se um dado bruto mudar, o gráfico muda junto. As versões em SVG e PNG, para os slides, ficam em `docs/assets/graficos/teste-usuarios/`.

## 1. Visão geral das métricas

[[GRAFICO_TU:painel-metricas]]

## 2. Conclusão e primeiro clique por tarefa

[[GRAFICO_TU:conclusao-por-tarefa]]

[[GRAFICO_TU:primeira-escolha]]

## 3. O caso do calendário acadêmico

[[GRAFICO_TU:trajetoria-t6]]

## 4. Tempo em relação a um especialista

[[GRAFICO_TU:tempo-vs-especialista]]

## 5. Percepção dos estudantes

[[GRAFICO_TU:percepcao-vs-desempenho]]

[[GRAFICO_TU:sus-por-participante]]

[[GRAFICO_TU:problemas-celular]]

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 21/11/2026 | Gráficos dos resultados do teste com usuários e do questionário | Caio Borges |
