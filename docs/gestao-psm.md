# Gestão do Projeto (PSM/CID)

O roteiro exige acompanhar a execução do projeto com métricas do PSM/CID nas categorias **Calendário e Progresso**, **Recursos e Custos** e **Desempenho dos Processos**, registrando as medições, a interpretação e as decisões de gestão decorrentes (premissa 3 e seção 2 do roteiro). Esta página define os indicadores, o procedimento de coleta e o histórico das medições.

Os indicadores seguem o modelo de informação do PSM (atributo, medida básica, medida derivada, indicador, critério de decisão) [1] e adaptam medidas especificadas no *framework* para desenvolvimento contínuo e iterativo (CID) [2].

## 1. Indicadores

*Tabela 1 - Indicadores de gestão do projeto.*

| ID | Categoria | Necessidade de informação | Medidas básicas | Indicador | Critério de decisão | Base no PSM/CID |
| -- | --------- | ------------------------- | --------------- | --------- | ------------------- | --------------- |
| I1 | Calendário e Progresso | Os artefatos de cada entrega serão concluídos no prazo? | Artefatos planejados para a entrega; artefatos integrados ao ramo `main` | % concluído = concluídos / planejados | Faltando uma semana para a entrega, conclusão abaixo de 80% exige redistribuição de tarefas | Committed vs. Completed (CID 8.3) |
| I2 | Calendário e Progresso | O trabalho restante está diminuindo no ritmo planejado? | *Issues* do marco da entrega abertas por dia | Curva de *burndown* real x planejada | Desvio maior que 10% em relação à linha planejada é discutido na reunião seguinte | Burndown (CID 8.2) |
| I3 | Recursos e Custos | O esforço está distribuído entre os membros? | Horas estimadas por membro a partir das palavras e linhas adicionadas em cada PR, mais horas fora do repositório registradas na planilha de esforço | Participação percentual de cada membro | Participação abaixo de 10% ou acima de 40% do total exige rebalanceamento | Personnel Effort (CID, ICM linha 10) |
| I4 | Desempenho dos Processos | A integração das fases é ágil? | Data/hora do primeiro *commit* do ramo; data/hora do *merge* do PR | Tempo de ciclo (h) | Ciclo maior que cinco dias indica integração tardia e risco de conflito | Cycle Time (CID 8.5) |
| I5 | Desempenho dos Processos | A revisão encontra problemas antes da integração? | Alterações do PR; correções feitas após comentários de revisão | % de retrabalho | Retrabalho acima de 30% motiva *checklist* de revisão baseado nos critérios do roteiro | Rework (CID, ICM linha 19) |

## 2. Procedimento de coleta

- **I1:** a lista de artefatos de cada entrega é fixada no início da fase (Tabela 2). Um artefato é concluído quando está integrado ao ramo `main`.
- **I2:** cada artefato vira uma *issue* no marco da entrega (E1 ou E2). O número de *issues* abertas é lido no painel de *milestones* do GitHub.
- **I3:** a partir da Entrega 2, coletado automaticamente pelo GitHub Actions. Cada PR recebe um comentário com as horas estimadas dos *commits* (palavras e linhas adicionadas convertidas pelas taxas da [metodologia de contribuição](contribuicao.md#32-coleta-automatica-a-partir-da-entrega-2)) e a participação de cada membro após o *merge*. O [dashboard de contribuição](gestao-esforco.md) é recalculado a cada publicação do site. Trabalho fora do repositório (reuniões, pesquisa) é registrado em `gestao/esforco.csv`, com evidência.
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

### Medição 2 - 03/11/2026 (fechamento da Entrega 1 e início da Entrega 2)

A medição 2 fecha a Entrega 1 (26/10/2026) e confere se as decisões da medição 1 foram executadas. As decisões novas seguem as ações da [retrospectiva da Entrega 1](assets/retrospectiva-e1.pdf) (28/10/2026), que definiu um responsável para cada indicador.

*Tabela 4 - Acompanhamento das decisões da medição 1.*

| Indicador | Decisão da medição 1 | Situação em 03/11/2026 |
| --------- | -------------------- | ---------------------- |
| I1 | Priorizar o artigo e a tabela de contribuição | Executada: os dois entraram na *release* 1.0 (PR #4 e *commits* de 25/10/2026) |
| I2 | Criar os marcos E1 e E2 e uma *issue* por artefato | Não executada: o GitHub não tem marcos nem *issues*. A retrospectiva repetiu a ação, com Caio como responsável |
| I3 | Adotar a planilha de esforço | Executada: `gestao/esforco.csv` e `gestao/esforco.py` (PR #4), com as horas da Entrega 1 estimadas na página [Contribuição](contribuicao.md) |
| I4 | Manter um ramo e um PR por fase | Parcial: os PRs #3 a #5 seguiram a regra, mas sete *commits* foram enviados direto ao ramo `main` entre 25 e 28/10/2026 (artigo, personas e retrospectiva) |
| I5 | Registrar a revisão como comentários nos PRs a partir da Fase 3 | Ainda não aplicável: nenhum PR da Fase 3 foi aberto |

*Tabela 5 - Resultado da medição 2.*

| Indicador | Valor | Interpretação | Decisão |
| --------- | ----- | ------------- | ------- |
| I1 | 17 de 17 artefatos (100%) na entrega; *release* 1.0 publicada em 25/10/2026 | Entrega 1 concluída no prazo | Na Entrega 2, fixar a lista de artefatos com prazos internos e acompanhar a situação toda semana (retrospectiva, ação C1; responsável: Caio) |
| I2 | Não mensurável | A decisão da medição 1 não foi executada, então ainda não há *burndown* | Criar o marco E2 e uma *issue* por artefato antes do início da Fase 3 (responsável: Caio) |
| I3 | Entrega 1: participação entre 13,9% e 18,8% (52,0 h estimadas). Entrega 2: nenhuma hora registrada até 03/11/2026 | A Entrega 1 está dentro do critério, mas 26% das horas foram declaradas pela equipe, sem evidência no Git. O registro da Entrega 2 ainda não começou | Registrar as horas de cada sessão de trabalho, com evidência (retrospectiva, ação C1; responsável: Felipe) |
| I4 | PRs #3, #4 e #5: 0,4 h, 27,8 h e 6,6 h | Todos abaixo do limite de cinco dias, mas sete *commits* não passaram por PR | Todo artefato entra no ramo `main` por PR |
| I5 | Não mensurável: 1 revisão formal (PR #3) em 5 PRs, sem comentários | As revisões não ficam registradas, então o retrabalho não pode ser medido | Todo PR é revisado por outro membro antes do *merge*, com comentários (retrospectiva, ação C2; responsável: Leonardo) |

*Fonte: PRs, release, marcos e issues do GitHub, `gestao/esforco.csv` e retrospectiva da Entrega 1, em 03/11/2026.*

## Referências

[1] McGARRY, J. et al. *Practical Software Measurement: Objective Information for Decision Makers*. Boston: Addison-Wesley, 2002.

[2] JONES, C. L. et al. *Practical Software and Systems Measurement Continuous Iterative Development Measurement Framework: Part 2 - Measurement Specifications and Enterprise Measures*. Versão 2.1. PSM, NDIA e INCOSE, 2021.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 19/10/2026 | Indicadores PSM/CID (I1 a I5), procedimento de coleta e medição 1 | [arthurlleite](https://github.com/arthurlleite) |
| 1.1 | 03/11/2026 | Medição 2: fechamento da Entrega 1 e acompanhamento das decisões da medição 1 | Caio Borges |
| 1.2 | 10/11/2026 | Coleta automática do I3 pelo GitHub Actions, por recomendação da professora na apresentação dos indicadores | Caio Borges |
