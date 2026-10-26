# Metodologia

Esta página reproduz a Metodologia de desenvolvimento do projeto do [artigo da Entrega 1](index.md).

## 1. Processo e organização do trabalho

A avaliação segue as quatro fases do processo de avaliação de produto ([Referencial Teórico](referencial-teorico.md#2-processo-de-avaliacao-de-produto)). A equipe atua como **avaliador independente**: não desenvolve nem opera o SIGAA e não tem acesso a código-fonte ou infraestrutura, o que torna a avaliação externa (caixa-preta).

O trabalho é organizado no repositório Git da disciplina (Tabela 1). As decisões são tomadas em reunião: cada membro elabora sua proposta, as propostas são consolidadas e as divergências discutidas até o consenso, como na [matriz Impacto x Risco](../fase-1/caracteristicas.md).

*Tabela 1 - Práticas de organização do trabalho.*

| Prática | Como é aplicada |
| ------- | --------------- |
| Ramos por fase | Cada fase é desenvolvida em um ramo próprio (`fase-1`, `fase-2`, `artigo-latex`) e integrada ao ramo principal por *pull request* (PR), após revisão por outro membro |
| Identificador de tarefa | Os *commits* recebem um identificador (`[D01]` a `[D10]` na Entrega 1), que permite rastrear cada alteração até a atividade de origem |
| Publicação | A documentação é publicada automaticamente como GitPage (MkDocs) a cada integração no ramo principal, junto com o [artigo em PDF](index.md) |
| Histórico | Cada página traz histórico de versões com data, descrição e autor |

*Fonte: elaborado pela equipe.*

## 2. Gestão do projeto com indicadores PSM/CID

O roteiro exige acompanhar o projeto com métricas do PSM/CID nas categorias calendário e progresso, recursos e custos e desempenho dos processos [1]. A Tabela 2 apresenta os indicadores, construídos segundo o modelo de informação do PSM [2] e adaptados do *framework* CID [3], com a primeira medição, feita em 19/10/2026 a partir do histórico do repositório, a sete dias da entrega. O procedimento de extração e os dados estão em [Gestão do Projeto](../gestao-psm.md).

*Tabela 2 - Indicadores PSM/CID e primeira medição (19/10/2026).*

| Categoria | Indicador (medidas) | Critério de decisão | Valor medido | Interpretação e decisão |
| --------- | ------------------- | ------------------- | ------------ | ----------------------- |
| Calendário e progresso | **I1** Comprometido vs. concluído: artefatos da entrega integrados ao ramo principal / planejados | < 80% a uma semana da entrega exige redistribuição de tarefas | 14 de 17 (82%): 14 páginas das Fases 1 e 2; artigo, contribuição e *release* pendentes | Dentro do critério. Priorizar o artigo e a tabela de contribuição |
| Calendário e progresso | **I2** *Burndown*: *issues* abertas do marco da entrega, por dia | Desvio > 10% da linha planejada é discutido em reunião | Não mensurável: nenhuma *issue* ou marco | Lacuna de processo. Criar marcos E1 e E2 e uma *issue* por artefato |
| Recursos e custos | **I3** Esforço por membro: horas na planilha de esforço e participação (%) | Participação < 10% ou > 40% exige rebalanceamento | Planilha não adotada; *proxy*: *commits* por membro = 9, 3, 3, 2 e 0 | *Commits* não medem esforço. Adotar a planilha, que alimenta a tabela de contribuição |
| Desempenho dos processos | **I4** Tempo de ciclo: primeiro *commit* do ramo até a integração do PR (h) | Ciclo > 5 dias indica integração tardia | Fase 1: 49,0 h; Fase 2: 16,7 h | Dentro do critério. Manter um ramo e um PR por fase |
| Desempenho dos processos | **I5** Retrabalho: correções após revisão / alterações do PR (%) | > 30% motiva *checklist* de revisão | Não medido: revisões não registradas | Registrar a revisão nos PRs a partir da Fase 3 |

*Fonte: elaborado pela equipe, com base em [2], [3] e no histórico do repositório.*

As decisões da Tabela 2 começaram a ser aplicadas antes da entrega. Para o I3, a equipe adotou a planilha de esforço em horas-pessoa (`gestao/esforco.csv`), com um *script* versionado que soma as horas e calcula a participação de cada membro (`gestao/esforco.py`). As horas da Entrega 1 foram reconstruídas por estimativa, e todos os membros ficaram entre 13,9% e 18,8%, dentro do critério de decisão ([Contribuição](../contribuicao.md)). A partir da Entrega 2, as horas são registradas por atividade e revisadas pela equipe.

## 3. Aspectos éticos e rastreabilidade

- Nenhuma tarefa altera dados acadêmicos: todas são consultas ou emissões de documentos feitas pelos participantes com as próprias credenciais.
- A participação em testes e no questionário é voluntária e precedida de termo de consentimento, e as sessões só são gravadas mediante consentimento [1].
- Os participantes são identificados por código (P1, P2, ...) e perfil, e capturas de tela têm os dados pessoais ocultados.
- Os dados brutos anonimizados, os consolidados e os procedimentos de cálculo ficarão na pasta `dados/` do repositório; as gravações terão acesso restrito à equipe e à professora.

## 4. Declaração de uso de inteligência artificial

A equipe usou o Claude Opus 5.5 (Claude Code) para: (a) apoiar a redação e a formatação das páginas da Fase 1; (b) apoiar a redação da Fase 2 e verificar a consistência entre as páginas e o roteiro; (c) pesquisar as características de qualidade oficiais e padronizadas da ISO/IEC 25010 e a padronização do IEEE (modelo IEEEtran) para a documentação em LaTeX; (d) propor a metodologia de esforço por horas e o *script* de cálculo; e (e) atualizar o artigo após os ajustes da Fase 2 e a inclusão das personas. O DeepSeek v4 foi usado na estruturação inicial do repositório. Todo conteúdo gerado foi conferido pela equipe contra as páginas do repositório e o roteiro; as referências foram verificadas uma a uma, e os números citados foram conferidos com as fontes originais. O registro completo está em [Uso de IA](../uso-de-ia.md).

## Referências

[1] RAMOS, C. S. *Projeto Final da Disciplina - Avaliação da Qualidade de Produto de Software*. FGA0315 Qualidade de Software 1, Universidade de Brasília, 2026.

[2] McGARRY, J. et al. *Practical Software Measurement: Objective Information for Decision Makers*. Boston: Addison-Wesley, 2002.

[3] JONES, C. L. et al. *Practical Software and Systems Measurement Continuous Iterative Development Measurement Framework: Part 2 - Measurement Specifications and Enterprise Measures*. Versão 2.1. PSM, NDIA e INCOSE, 2021.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 26/10/2026 | Conteúdo da Metodologia, a partir do artigo da Entrega 1 | [arthurlleite](https://github.com/arthurlleite) |
