# Cronograma da Avaliação e Plano de Ação da Entrega 2

<!-- Critério F3-C3: O cronograma é realista e alinha as ações à execução da Fase 4. -->

<!-- Critério F3-C8: Consistência entre as Fases 2 e 3 (rastreabilidade total e justificada). -->

<!-- Entrega 2: 22/11/2026. Ponto de Controle 2 (PC2): release até 15/11/2026, 23h59; apresentação em 16/11/2026. Coordenação das entrevistas: Leonardo Fachinello Bonetti. -->

Este documento estabelece o **cronograma operacional da Entrega 2**, cujo prazo de submissão é **22/11/2026**, com o **Ponto de Controle 2 (PC2)** no meio do caminho: release do PC2 no repositório até **15/11/2026, às 23h59**, e apresentação à professora em **16/11/2026**. Ele organiza as ações das **Fases 3 (Projeto da Avaliação)** e **4 (Execução e Julgamento)** da norma **ISO/IEC 25040**, a condução do **teste com usuários com estudantes do começo e do meio ou fim do curso** (coordenado por **Leonardo Fachinello Bonetti**), o planejamento da **Ação de Melhoria Técnica Obrigatória**, a **2ª versão do Artigo Científico em LaTeX** e o fechamento da **Gestão do Projeto (PSM/CID)**.

---

## 1. Janela Operacional e Marcos Críticos (Até 22/11/2026)

Com o PC2 em 15 e 16/11/2026 e a Entrega 2 em **22/11/2026**, as atividades estão organizadas em uma escala diária de execução:

```mermaid
gantt
    title Plano de Ação - Entrega 2 (PC2: 15-16/11; Entrega: 22/11/2026)
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m
    inclusiveEndDates
    section Fase 3: Planejamento
    Protocolo, ambiente, planilhas e TCLE       :done, 2026-11-11, 2026-11-14
    section Fase 4: Coleta
    Teste com usuários (Coord. Leonardo)        :active, 2026-11-13, 2026-11-16
    Inspeções por pares e matriz de navegadores :2026-11-13, 2026-11-16
    Consolidação dos dados brutos (dados/)      :2026-11-16, 2026-11-17
    section Ponto de Controle 2
    Release do PC2                              :milestone, 2026-11-15, 0d
    Apresentação e artigo no Moodle             :2026-11-15, 2026-11-16
    section Fase 4: Análise e Julgamento
    Cálculo das métricas                        :2026-11-17, 2026-11-18
    Julgamento e verificação de hipóteses       :2026-11-18, 2026-11-19
    Coerência com o propósito da Fase 1         :2026-11-19, 2026-11-19
    section Ação de Melhoria
    Seleção e execução da melhoria              :2026-11-19, 2026-11-20
    Documentação da melhoria                    :2026-11-20, 2026-11-21
    section Finalização e Entrega
    Artigo LaTeX v2 (Resultados e Conclusão)    :2026-11-20, 2026-11-22
    GitPage e tabela de contribuição            :2026-11-20, 2026-11-22
    Revisão final, release v2.0 e submissão     :2026-11-22, 2026-11-22
```

*Figura 1 — Linha do tempo da Entrega 2, com o PC2 em 15 e 16/11/2026 e a entrega em 22/11/2026. Fonte: elaboração da equipe.*

---

## 2. Teste com Usuários

O teste com usuários segue o [Protocolo do Teste com Usuários](teste-usuarios.md), sob a coordenação geral de **Leonardo Fachinello Bonetti**. São **6 participantes**, em dois grupos de três que diferem apenas no semestre, e **todos executam as tarefas T1 a T6** na mesma sessão, na ordem rotacionada do protocolo. Ao fim de cada sessão, o participante responde o SUS e o [questionário](../fase-2/questionario.md):

1. **Começo do curso (1º e 2º semestres):** perfil calouro da Fase 1, com atenção à apreensibilidade e à compreensão da terminologia institucional (IRA, menções, código de horário).
2. **Meio ou fim do curso (5º semestre em diante):** perfis veterano e formando, com atenção à integralização curricular, à carga horária pendente e à emissão de documentos.

Estudantes do 3º e do 4º semestre não são recrutados. O uso no celular não faz parte das sessões: é avaliado por inspeção da equipe nas métricas M14 e M15 (T08).

*Tabela 1 — Planejamento do teste com usuários (Coordenação: Leonardo Fachinello Bonetti).*

| Grupo                                                   |   Participantes   | Tarefas | Período de Realização | Instrumentos e Registro                                                 | Responsável pela Condução  |
| :------------------------------------------------------ | :---------------: | :-----: | :----------------------: | :---------------------------------------------------------------------- | :---------------------------- |
| **Começo do curso** (1º e 2º semestres)        | 3, mais 1 reserva | T1 a T6 | 13/11/2026 a 16/11/2026 | Roteiro do protocolo, gravação consentida (TCLE), SUS e questionário | Caio Borges / Daniel Duarte   |
| **Meio ou fim do curso** (5º semestre em diante) | 3, mais 1 reserva | T1 a T6 | 13/11/2026 a 16/11/2026 | Roteiro do protocolo, gravação consentida (TCLE), SUS e questionário | Leonardo Bonetti / Davi Nobre |

---

## 3. Matriz de Tarefas da Entrega 2 (Programado vs. Efetivamente Feito)

A Tabela 2 apresenta as atividades com prazos diários até a entrega em **22/11/2026**, incluindo as entregas do PC2 (pacote E2-PC2), e serve de base para auditar o **programado contra o efetivamente executado**.

**Atualização de fechamento (23/11/2026):** os estados abaixo foram revistos com base nos artefatos versionados. Quando a data ou a confirmação dependem de registros externos (Moodle, gravações ou planilha de horas), não foram deduzidos do histórico Git. T20 permanece pendente: não há relatos individuais nem apêndice correspondente no artigo/repositório.

*Tabela 2 — Cronograma operacional detalhado para a Entrega 2 (PC2: 15 e 16/11/2026; prazo final: 22/11/2026).*

|        ID        | Pacote / Atividade                                               | Responsável               |  Início  |      Fim Plan.      | Esforço (h) |                Status                |  Fim Real  | Esforço Real | Desvio / Observações                                                                                                                         |
| :--------------: | :--------------------------------------------------------------- | :------------------------- | :--------: | :------------------: | :----------: | :-----------------------------------: | :--------: | :-----------: | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| **E2-F3** | **Fase 3 — Projeto da Avaliação**                       |                            |            |                      |              |                                      |            |              |                                                                                                                                                |
|       T01       | Formalização do Cronograma da E2                               | Davi Nobre                 | 10/11/2026 |      12/11/2026      |    3,0 h    |         **Concluído**         | 12/11/2026 |      —      | Prazo revisto em 14/11/2026: PC2 em 15 e 16/11 e entrega em 22/11 (v1.3)                                                                       |
|       T02       | Elaboração dos POPs e Métodos de Coleta (F3-C1)               | Leonardo Bonetti           | 11/11/2026 |      13/11/2026      |    4,0 h    |         **Concluído**         | 14/11/2026 |      —      | [Protocolo do Teste com Usuários](teste-usuarios.md) e [Planilhas de Coleta](planilhas.md) (PR #14); 1 dia de atraso                            |
|       T03       | Especificação de Ambientes, Telas e Dados (F3-C2)              | Davi Nobre                 | 11/11/2026 |      13/11/2026      |    3,0 h    |         **Concluído**         | 14/11/2026 |      —      | [Recursos e Ambiente](recursos-ambiente.md) (PR #13), executada por Felipe Campêlo; 1 dia de atraso                                            |
|       T04       | Roteiro do Moderador e TCLE para Entrevistas                     | Daniel Duarte              | 11/11/2026 |      13/11/2026      |    4,0 h    |         **Concluído**         | 14/11/2026 |      —      | Roteiro da sessão e termo de consentimento (PR #14), executada por Leonardo Bonetti; 1 dia de atraso                                          |
|       T05       | Matriz de Rastreabilidade Fase 2 → Fase 3 (F3-C8)               | Leonardo Bonetti           | 12/11/2026 |      14/11/2026      |    2,5 h    |         **Concluído**         | 14/11/2026 |      —      | Tabelas 2 e 3 da [página da Fase 3](index.md) (PR #14)                                                                                         |
| **E2-F4A** | **Fase 4 — Teste com Usuários e Coleta de Dados Brutos** |                            |            |                      |              |                                      |            |              |                                                                                                                                                |
|       T06       | **Coordenação e Condução do Teste com Usuários**      | **Leonardo Bonetti** | 13/11/2026 |      16/11/2026      |    10,0 h    |         **Concluído**         | 16/11/2026 |      —      | Seis sessões previstas: cinco realizadas (P1, P2, P3, P4 e P6), conforme dados e resultados da Fase 4                                         |
|       T07       | Execução das Inspeções por Pares (M1, M2, M10, M20)          | Daniel / Davi              | 13/11/2026 |      16/11/2026      |    6,0 h    |         **Concluído**         | 22/11/2026 |      —      | Inspeções e julgamentos documentados em Fase 4; dois avaliadores conforme registros do método                                               |
|       T08       | Testes em Matriz de Navegadores e Telas (M13 a M15)              | Felipe Campêlo            | 13/11/2026 |      16/11/2026      |    5,0 h    |         **Concluído**         | 22/11/2026 |      —      | M13–M15 documentadas; M15 executada em celular real em 22/11                                                                                  |
|       T09       | Organização e Anonimização dos Dados Brutos (`dados/`)     | Caio Borges                | 16/11/2026 |      17/11/2026      |    4,0 h    |         **Concluído**         | 23/11/2026 |      —      | Dados anonimizados e consolidados em `dados/`; gravações ficam na pasta restrita prevista no protocolo                                     |
| **E2-PC2** | **Ponto de Controle 2**                                    |                            |            |                      |              |                                      |            |              |                                                                                                                                                |
|       P01       | Release do PC2 no repositório                                   | Davi Nobre                 | 15/11/2026 |      15/11/2026      |    0,5 h    |    **Concluído com atraso**    | 16/11/2026 |      —      | Tag `Entrega2` criada em 16/11/2026; não comprova envio no Moodle                                                                           |
|       P02       | Apresentação do PC2 (PDF no Moodle)                            | Toda a equipe              | 15/11/2026 |      16/11/2026      |    4,0 h    |               Planejado               |     —     |      —      | Até 13h30 de 16/11 (T02); no máximo 15 min, foco nas Fases 3 e 4, 1 ou 2 slides de gestão e link da release do PC2                          |
|       P03       | Artigo no estágio atual no Moodle                               | Arthur Leite               | 16/11/2026 |      16/11/2026      |    1,0 h    |               Planejado               |     —     |      —      | Sem exigência de seções concluídas                                                                                                         |
| **E2-F4B** | **Fase 4 — Análise, Julgamento e Hipóteses**            |                            |            |                      |              |                                      |            |              |                                                                                                                                                |
|       T10       | Tabulação e Cálculo das Métricas                             | Leonardo Bonetti           | 17/11/2026 |      18/11/2026      |    5,0 h    |         **Concluído**         | 22/11/2026 |      —      | Métricas da avaliação registradas em `dados/consolidados/metricas.csv` e páginas da Fase 4                                               |
|       T11       | Confronto com Níveis de Pontuação e Julgamento                | Daniel Duarte              | 18/11/2026 |      19/11/2026      |    4,0 h    |         **Concluído**         | 22/11/2026 |      —      | Julgamento documentado para G1, G2 e G3                                                                                                        |
|       T12       | Verificação de Hipóteses (H1 a H16, HR1, HR2)                 | Felipe Campêlo            | 18/11/2026 |      19/11/2026      |    3,5 h    |         **Concluído**         | 22/11/2026 |      —      | Classificações registradas na página de julgamento                                                                                          |
|       T13       | Análise de Coerência com o Propósito da Fase 1                | Caio Borges                | 19/11/2026 |      19/11/2026      |    3,0 h    |         **Concluído**         | 22/11/2026 |      —      | Síntese final relaciona resultados às decisões apoiadas                                                                                     |
| **E2-MEL** | **Ação de Melhoria Técnica Obrigatória**               |                            |            |                      |              |                                      |            |              |                                                                                                                                                |
|       T14       | Seleção da oportunidade crítica pós-julgamento               | Toda a equipe              | 19/11/2026 |      19/11/2026      |    2,5 h    |         **Concluído**         | 21/11/2026 |      —      | Selecionada melhoria do fluxo mobile com base nos resultados de M14/M9 e tarefas críticas                                                     |
|       T15       | Execução Técnica da Ação de Melhoria                        | Davi / Arthur              | 19/11/2026 |      20/11/2026      |    8,0 h    |         **Concluído**         | 23/11/2026 |      —      | Protótipo executável documentado em `fase-4/prototipo-mobile.md` e arquivos de `docs/assets/prototipo-mobile/`                           |
|       T16       | Documentação técnica e justificativa da melhoria              | Daniel Duarte              | 20/11/2026 |      21/11/2026      |    3,5 h    |         **Concluído**         | 23/11/2026 |      —      | Resultados medidos de M14/M9 e limitações documentados; validação de M5/M6/M12 ainda é futura                                             |
| **E2-ART** | **Artigo Científico v2, GitPage e Release**               |                            |            |                      |              |                                      |            |              |                                                                                                                                                |
|       T17       | Redação de Resultados e Discussão no Artigo IEEE              | Leonardo / Caio            | 20/11/2026 |      21/11/2026      |    6,0 h    |         **Concluído**         | 23/11/2026 |      —      | Resultados e discussão presentes no artigo consolidado                                                                                        |
|       T18       | Redação da Ação de Melhoria e Conclusão no Artigo           | Arthur Leite               | 21/11/2026 |      22/11/2026      |    4,0 h    |         **Concluído**         | 23/11/2026 |      —      | Seções de melhoria e conclusão presentes no artigo                                                                                          |
|       T19       | Atualização da GitPage com Fases 3 e 4 completas               | Davi Nobre                 | 20/11/2026 |      22/11/2026      |    5,0 h    |         **Concluído**         | 23/11/2026 |      —      | Páginas da avaliação e síntese final integradas                                                                                            |
|       T20       | Apêndice de Contribuição Individual (total 100%)              | Felipe Campêlo            | 21/11/2026 |      22/11/2026      |    2,5 h    |          **Pendente**          |     —     |      —      | Faltam os relatos individuais; horas/atividades da tabela existente não substituem os relatos nem formam o apêndice exigido                  |
|       T21       | Revisão Final e Compilação do Artigo em LaTeX                 | Toda a equipe              | 22/11/2026 |      22/11/2026      |    3,0 h    |         **Concluído**         | 23/11/2026 |      —      | PDF e fontes finais versionados; fechamento no repositório posterior à data planejada                                                        |
|       T22       | **Publicação da Release v2.0 e Submissão Moodle**       | Davi Nobre                 | 22/11/2026 | **22/11/2026** |    2,0 h    | **Parcial / não verificável** |     —     |      —      | Artefatos finais estão no repositório; tag e comprovante de submissão Moodle não foram localizados como evidência da release oficial v2.0 |

*Fonte: elaboração da equipe (2026). Nota: Os valores da coluna "Esforço Real" são consolidados a partir das medições automáticas do GitHub Actions (word-diff em PRs) e dos apontamentos de atividades extracódigo em `gestao/esforco.csv` (como entrevistas e reuniões). As tarefas do PC2 usam o prefixo P para não renumerar as tarefas T10 a T22, já citadas pela equipe.*

---

## 4. Ação de Melhoria Obrigatória (Critério de Seleção)

Conforme a seção 3.2 do roteiro da disciplina, a equipe deve executar obrigatoriamente pelo menos uma ação de melhoria técnica, justificada com base nas evidências obtidas na Fase 4.

A equipe avaliará os resultados da avaliação no dia **19/11/2026** (T14), depois do julgamento, para deliberar entre as quatro opções previstas pelo roteiro:

1. **Elaboração de protótipo:** caso o problema crítico se concentre na interface, usabilidade ou fluxo de navegação do discente.
2. **Modificação direta de código ou extensão técnica:** caso o problema seja passível de correção direta em código client-side ou script auxiliar (por exemplo, extensão de navegador ou userscript), sem necessidade de acesso ao código-fonte do SIGAA.
3. **Templates técnicos:** caso o problema seja ausência ou fragilidade de documentação/padronização.
4. **Proposição de processo:** caso seja identificado um vício de processo recorrente.

O grupo Adele Goldstine não possui acesso ao código-fonte fechado do SIGAA. Dessa forma, ficam descartadas quaisquer opções que dependam de modificação direta nos servidores ou no repositório interno do sistema. Contudo, soluções que atuem exclusivamente no lado do cliente, como extensões de navegador ou userscripts, permanecem viáveis, uma vez que não requerem acesso ao código-fonte da aplicação.

---

## 5. Rastreabilidade com os Indicadores PSM/CID

A validação do **programado vs. efetivamente feito** é aferida diariamente até o dia **22/11/2026**:

1. **I1 (% Concluído):** medido pela razão de tarefas concluídas sobre as 25 planejadas na Tabela 2 (T01 a T22 e P01 a P03). As metas contam as tarefas cujo fim planejado é até a data.
   - Meta em 15/11/2026: 24% (T01 a T05 e P01 — Fase 3 fechada e release do PC2).
   - Meta em 16/11/2026: 44% (mais T06 a T08, P02 e P03 — coleta concluída e PC2 apresentado).
   - Meta em 19/11/2026: 68% (mais T09 a T14 — dados organizados, métricas, julgamento, hipóteses e seleção da melhoria).
   - Meta em 22/11/2026: 100% (Release v2.0 e submissão no Moodle).
2. **I2 (Burndown de Issues):** ainda não há *milestone* nem *issues* no repositório, então o *burndown* não pode ser medido (lacuna já registrada em [Gestão do Projeto](../gestao-psm.md)). Enquanto a gestão não decidir criá-los, o acompanhamento é feito pelo status da Tabela 2 e pelos PRs.
3. **I3 (Esforço por Membro):** monitorado pela estimativa automática de horas via GitHub Actions (word-diff em PRs) e complementado por registros manuais na planilha `gestao/esforco.csv` para atividades fora do Git (entrevistas, inspeções presenciais e reuniões), conforme metodologia descrita na [página de Contribuição](../contribuicao.md).

---

## Histórico de Versão

| Versão |    Data    |                                                                                                                                                Descrição                                                                                                                                                |                  Autor                  |
| :-----: | :--------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------: |
|   1.0   | 12/11/2026 |                                                                        Criação do cronograma detalhado da Entrega 2 alinhado à data fatal de 18/11/2026 e com foco nas entrevistas coordenadas por Leonardo Fachinello Bonetti                                                                        | [Davi Nobre](https://github.com/Jagaima) |
|   1.1   | 12/11/2026 |                                                                          Remoção do questionário online, formatação de todas as datas no padrão brasileiro (DD/MM/AAAA) e flexibilização da ação de melhoria técnica                                                                          | [Davi Nobre](https://github.com/Jagaima) |
|   1.2   | 12/11/2026 |                                                            Correções da revisão de PR: dateFormat do Gantt, alinhamento de datas entre tabelas, metas do I1, escopo da exclusão de melhorias, descrição do I3 e parágrafo da seção 4                                                            | [Davi Nobre](https://github.com/Jagaima) |
|   1.3   | 14/11/2026 | Entrega em 22/11/2026 e PC2 em 15 e 16/11 (tarefas P01 a P03); teste com usuários alinhado ao protocolo (2 grupos de 3, T1 a T6, até 16/11); datas da análise sem sobreposição; status de T02 a T06; H1 a H16 em T12; metas do I1 recalculadas; I2 sem *milestone*; `inclusiveEndDates` no Gantt |               Caio Borges               |
|   1.4   | 23/11/2026 |                                                                                   Atualização dos estados de execução com evidências do repositório; registro de T20 pendente e de T22 sem comprovação externa                                                                                   |           Daniel Nunes Duarte           |
