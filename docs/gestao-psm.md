# Gestão do Projeto (PSM/CID)

O roteiro exige acompanhar a execução do projeto com métricas do PSM/CID nas categorias **Calendário e Progresso**, **Recursos e Custos** e **Desempenho dos Processos**, registrando as medições, a interpretação e as decisões de gestão decorrentes (premissa 3 e seção 2 do roteiro). Esta página define os indicadores, o procedimento de coleta e o histórico das medições.

Os indicadores seguem o modelo de informação do PSM (atributo, medida básica, medida derivada, indicador, critério de decisão) [1] e adaptam medidas especificadas no *framework* para desenvolvimento contínuo e iterativo (CID) [2].

## 1. Indicadores

*Tabela 1 - Indicadores de gestão do projeto.*

| ID | Categoria | Necessidade de informação | Medidas básicas | Indicador | Critério de decisão | Base no PSM/CID |
| -- | --------- | ------------------------- | --------------- | --------- | ------------------- | --------------- |
| I1 | Calendário e Progresso | Os artefatos de cada entrega serão concluídos no prazo? | Artefatos planejados para a entrega; artefatos integrados ao ramo `main` | % concluído = concluídos / planejados | Faltando uma semana para a entrega, conclusão abaixo de 80% exige redistribuição de tarefas | Committed vs. Completed (CID 8.3) |
| I2 | Calendário e Progresso | O trabalho restante está diminuindo no ritmo planejado? | *Issues* do marco da entrega abertas por dia | Curva de *burndown* real x planejada | Desvio maior que 10% em relação à linha planejada é discutido na reunião seguinte | Burndown (CID 8.2) |
| I3 | Recursos e Custos | O esforço está distribuído entre os membros? | Horas registradas por membro na planilha de esforço | Participação percentual de cada membro | Participação abaixo de 10% ou acima de 40% do total exige rebalanceamento | Personnel Effort (CID, ICM linha 10) |
| I4 | Desempenho dos Processos | A integração das fases é ágil? | Data/hora do primeiro *commit* do ramo; data/hora do *merge* do PR | Tempo de ciclo (h) | Ciclo maior que cinco dias indica integração tardia e risco de conflito | Cycle Time (CID 8.5) |
| I5 | Desempenho dos Processos | A revisão encontra problemas antes da integração? | Alterações do PR; correções feitas após comentários de revisão | % de retrabalho | Retrabalho acima de 30% motiva *checklist* de revisão baseado nos critérios do roteiro | Rework (CID, ICM linha 19) |

## 2. Procedimento de coleta

- **I1:** a lista de artefatos de cada entrega é fixada no início da fase (Tabela 2). Um artefato é concluído quando está integrado ao ramo `main`.
- **I2:** cada artefato vira uma *issue* no marco da entrega (E1 ou E2). O número de *issues* abertas é lido no painel de *milestones* do GitHub.
- **I3:** cada membro registra, ao fim de cada sessão de trabalho, data, horas, atividade e artefato em `gestao/esforco.csv`. O mesmo registro alimenta a [Tabela de Contribuição](contribuicao.md).
- **I4:** extraído do histórico Git com o comando abaixo, para cada ramo de fase.
- **I5:** contado nos PRs: alterações feitas após a primeira rodada de revisão sobre o total de *commits* do PR.

```bash
# Primeiro commit de um ramo de fase e data do merge correspondente
git log origin/fase-1 --reverse --format='%ad %h %s' --date=iso | head -1
git log main --merges --format='%ad %h %s' --date=iso | grep fase-1
# Commits por autor, sem merges
git log --all --no-merges --format='%an' | sort | uniq -c
```

## 3. Medições

### Medição 1 - 19/10/2026 (Entrega 1, a sete dias do prazo)

*Tabela 2 - Artefatos planejados para a Entrega 1 (I1).*

| Artefato | Situação em 19/10/2026 |
| -------- | ---------------------- |
| Fase 1: 7 páginas (síntese, propósito, software avaliado, modelo de qualidade, características, escopo, ODS) | Concluídas (PR #1, 18/10/2026) |
| Fase 2: 7 páginas (síntese, objetivos, questões, hipóteses, métricas, níveis de pontuação, gráfico GQM) | Concluídas (PR #2, 18/10/2026) |
| Artigo em LaTeX (Introdução, Referencial, Metodologia, Fases 1 e 2) | Em andamento |
| Tabela de contribuição | Pendente |
| *Release* E1 | Pendente |

*Tabela 3 - Resultado da medição 1.*

| Indicador | Valor | Interpretação | Decisão |
| --------- | ----- | ------------- | ------- |
| I1 | 14 de 17 artefatos (82%) | Acima do limite de 80% a sete dias da entrega | Priorizar o artigo e a tabela de contribuição, que dependem de todos os membros |
| I2 | Não mensurável | Nenhuma *issue* ou marco criado: lacuna de processo | Criar os marcos E1 e E2 e uma *issue* por artefato, para medir o *burndown* a partir da Fase 3 |
| I3 | Planilha não adotada. *Proxy*: *commits* sem *merge* por membro = 9, 3, 3, 2 e 0 | *Commits* não medem esforço: reuniões, pesquisa e revisão não aparecem no Git | Adotar a planilha de esforço; a tabela de contribuição usará as horas registradas |
| I4 | Fase 1: 49,0 h (16/10 13:37 a 18/10 14:36); Fase 2: 16,7 h (18/10 04:10 a 18/10 20:52) | Ambos abaixo do limite de cinco dias | Manter um ramo e um PR por fase |
| I5 | Não medido | Os PRs não registraram rodadas de revisão | Registrar a revisão como comentários nos PRs a partir da Fase 3 |

*Fonte: histórico do repositório em 19/10/2026.*

## Referências

[1] McGARRY, J. et al. *Practical Software Measurement: Objective Information for Decision Makers*. Boston: Addison-Wesley, 2002.

[2] JONES, C. L. et al. *Practical Software and Systems Measurement Continuous Iterative Development Measurement Framework: Part 2 - Measurement Specifications and Enterprise Measures*. Versão 2.1. PSM, NDIA e INCOSE, 2021.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 19/10/2026 | Indicadores PSM/CID (I1 a I5), procedimento de coleta e medição 1 | Arthur Leite |
