# Objetivos

Os objetivos de medição representam o **nível conceitual** do GQM. Cada objetivo foi escrito no template proposto por Basili, Caldiera e Rombach [1], que exige cinco elementos: objeto de estudo, propósito, foco de qualidade, ponto de vista e contexto.

Foi definido um objetivo para cada uma das três características avaliadas, dentre as priorizadas na [Fase 1](../fase-1/caracteristicas.md#3-caracteristicas-selecionadas) (Tabelas 1 a 3). O foco de qualidade de cada objetivo é a característica da ISO/IEC 25010:2023 [2]. As subcaracterísticas mantidas na [adaptação do modelo de qualidade](../fase-1/modelo-qualidade.md#2-adaptacoes-ao-contexto-do-sigaa) são tratadas pelas questões de cada objetivo, na página [Questões](questoes.md). As subcaracterísticas removidas na Fase 1, e a justificativa de cada remoção, estão naquela página e não são repetidas aqui.

A numeração G1 a G3 não segue a ordem de prioridade da Fase 1. Na [matriz Impacto x Risco](../fase-1/caracteristicas.md#3-caracteristicas-selecionadas), a ordem de prioridade entre as características avaliadas é: Capacidade de Interação (G2, P = 25), Adequação Funcional (G1, P = 20) e Flexibilidade (G3, P = 16). Eficiência de Desempenho também foi priorizada na Fase 1 (P = 16), mas ficou fora desta especificação por orientação da professora no ponto de controle. Essa ordem de prioridade é a usada na apresentação dos resultados da Fase 4 (regra 5 de [Níveis de Pontuação](niveis-pontuacao.md#regra-5-ausencia-de-nota-unica)).

Em todos os objetivos, a avaliação é de caixa-preta, feita na interface em produção e sem alteração de dados acadêmicos, conforme as [implicações para a avaliação](../fase-1/software-avaliado.md#5-implicacoes-para-a-avaliacao) registradas na Fase 1.

O contexto, igual em todos os objetivos, é o ambiente em que a avaliação é conduzida. Os elementos que delimitam a avaliação foram definidos na Fase 1 e não são repetidos no template: a versão do sistema e o período de observação, no [objeto da avaliação](../fase-1/escopo.md#1-objeto-da-avaliacao); as tarefas T1 a T6, nas [tarefas representativas](../fase-1/escopo.md#21-tarefas-representativas); e os navegadores, dispositivos, tamanhos de tela e redes, nos [ambientes de execução](../fase-1/escopo.md#22-ambientes-de-execucao). As observações preliminares OP-01 a OP-08, citadas nas justificativas, estão em [Software Avaliado](../fase-1/software-avaliado.md#4-observacoes-preliminares-da-interface).

## G1 - Adequação Funcional

*Tabela 1 - Objetivo de medição G1 - Adequação Funcional.*

| Elemento | Definição |
| -------- | --------- |
| **Analisar** | o portal do discente de graduação do SIGAA/UnB |
| **com o propósito de** | avaliar |
| **com respeito à** | adequação funcional |
| **do ponto de vista do** | estudante de graduação da UnB |
| **no contexto** | da disciplina Qualidade de Software 1 (FGA0315), no campus FCTE (Gama) da UnB |

A adequação funcional é caracterizada pelas subcaracterísticas completude funcional, correção funcional e pertinência funcional, cada uma tratada por questões próprias.

**Justificativa:** Adequação Funcional ficou em segundo lugar na matriz Impacto x Risco (P = 20). O estudante depende do SIGAA para tarefas sem alternativa institucional, e a existência de ferramentas comunitárias para planejar o fluxo (OP-07) indica lacunas de completude. G1 verifica, nas tarefas T1 a T6 e no planejamento do fluxo de disciplinas, se as funções necessárias existem, se produzem informações corretas e se bastam para a tarefa sem recurso a ferramentas externas.

## G2 - Capacidade de Interação (Usabilidade)

*Tabela 2 - Objetivo de medição G2 - Capacidade de Interação.*

| Elemento | Definição |
| -------- | --------- |
| **Analisar** | o portal do discente de graduação do SIGAA/UnB |
| **com o propósito de** | avaliar |
| **com respeito à** | usabilidade (capacidade de interação) |
| **do ponto de vista do** | estudante de graduação da UnB |
| **no contexto** | da disciplina Qualidade de Software 1 (FGA0315), no campus FCTE (Gama) da UnB |

A capacidade de interação é caracterizada pelas subcaracterísticas reconhecimento de adequação, apreensibilidade, operabilidade, proteção contra erros do usuário, inclusividade e autodescritividade, cada uma tratada por questões próprias, e é complementada pela satisfação (qualidade em uso).

**Justificativa:** Capacidade de Interação é a característica de maior prioridade na Fase 1 (P = 25) e a que reúne mais observações preliminares (OP-01 a OP-06). G2 verifica, na execução das tarefas T1 a T6 em computador, se o estudante localiza as funções, aprende a usá-las sem ajuda, conclui as tarefas com esforço razoável, recupera-se de erros, encontra barreiras de acessibilidade e compreende as informações sem legenda externa. Dois [perfis da Fase 1](../fase-1/proposito-stakeholders.md#22-perfis-de-usuarios-considerados) recebem atenção especial: os calouros, que no primeiro contato ainda desconhecem a terminologia acadêmica e a organização dos menus (apreensibilidade), e os estudantes com deficiência, que dependem de recursos de acessibilidade (inclusividade).

## G3 - Flexibilidade (Portabilidade)

*Tabela 3 - Objetivo de medição G3 - Flexibilidade.*

| Elemento | Definição |
| -------- | --------- |
| **Analisar** | o portal do discente de graduação do SIGAA/UnB |
| **com o propósito de** | avaliar |
| **com respeito à** | flexibilidade |
| **do ponto de vista do** | estudante de graduação da UnB |
| **no contexto** | da disciplina Qualidade de Software 1 (FGA0315), no campus FCTE (Gama) da UnB |

**Justificativa:** Flexibilidade obteve P = 16 na Fase 1. O layout de largura fixa e os menus acionados pela passagem do ponteiro (OP-02 e OP-03) podem impedir o estudante que só usa o celular de concluir suas tarefas, e por isso esse [perfil da Fase 1](../fase-1/proposito-stakeholders.md#22-perfis-de-usuarios-considerados) é o destaque deste objetivo. G3 verifica se o SIGAA funciona da mesma forma nos navegadores Chrome, Firefox, Edge e Safari, em computador, tablet e celular e com interação por mouse e por toque, conforme os [ambientes de execução](../fase-1/escopo.md#22-ambientes-de-execucao) da Fase 1.

## Referências

[1] BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994.

[2] ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 17/10/2026 | Definição dos objetivos G1, G2 e G3 no template GQM | Felipe Campêlo |
| 1.2 | 18/10/2026 | Numeração e legendas de tabelas; propósito dos objetivos; recortes da Usabilidade e da Portabilidade | Felipe Campêlo |
| 2.0 | 18/10/2026 | Alinhamento à Fase 1 reestruturada: objetivo G4 (Eficiência de Desempenho), nomenclatura da ISO/IEC 25010:2023 e subcaracterísticas mantidas na Fase 1 | Felipe Campêlo |
| 2.1 | 18/10/2026 | Satisfação declarada no foco de qualidade de G2 | Felipe Campêlo |
| 2.2 | 18/10/2026 | Integração da versão complementar: prioridade de cada objetivo na Fase 1, avaliação caixa-preta e vínculo de G4 com o ODS 10 | Leonardo Bonetti |
| 2.3 | 25/10/2026 | Remoção do objetivo G4 (Eficiência de Desempenho); prioridade das três características avaliadas | Leonardo Bonetti |
| 2.4 | 25/10/2026 | Propósito dos objetivos reduzido ao verbo "avaliar" | Leonardo Bonetti |
| 2.5 | 25/10/2026 | Mesmo objeto de estudo em G1 a G3: "o portal do discente de graduação do SIGAA/UnB" | Leonardo Bonetti |
| 2.6 | 25/10/2026 | Foco de qualidade de G2 e G3 reduzido à característica; subcaracterísticas de G2 em frase abaixo da tabela | Leonardo Bonetti |
| 2.7 | 25/10/2026 | Foco de qualidade de G1 reduzido à característica; subcaracterística *functional appropriateness* nomeada pertinência funcional | Leonardo Bonetti |
| 2.8 | 25/10/2026 | Ponto de vista único em G1 a G3 (estudante de graduação da UnB); destaque aos perfis movido para as justificativas de G2 e G3 | Leonardo Bonetti |
| 2.9 | 25/10/2026 | Contexto dos objetivos como ambiente da avaliação; versão, período, tarefas e ambientes remetidos à Fase 1; recortes de tarefa, dispositivo e navegador nas justificativas | Leonardo Bonetti |
