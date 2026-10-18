# Objetivos

Os objetivos de medição representam o **nível conceitual** do GQM. Cada objetivo foi escrito no template proposto por Basili, Caldiera e Rombach [1], que exige cinco elementos: objeto de estudo, propósito, foco de qualidade, ponto de vista e contexto.

Foi definido um objetivo para cada uma das quatro características priorizadas na [Fase 1](../fase-1/caracteristicas.md#3-caracteristicas-selecionadas) (Tabelas 1 a 4). O foco de qualidade de cada objetivo usa as subcaracterísticas da ISO/IEC 25010:2023 [2] mantidas na [adaptação do modelo de qualidade](../fase-1/modelo-qualidade.md#2-adaptacoes-ao-contexto-do-sigaa). As subcaracterísticas removidas na Fase 1, e a justificativa de cada remoção, estão naquela página e não são repetidas aqui.

## G1 - Adequação Funcional

*Tabela 1 - Objetivo de medição G1 - Adequação Funcional.*

| Elemento | Definição |
| -------- | --------- |
| **Analisar** | o portal do discente de graduação do SIGAA/UnB |
| **com o propósito de** | avaliar, a fim de identificar pontos fracos |
| **com respeito à** | adequação funcional (completude funcional, correção funcional e adequação funcional, ou pertinência) |
| **do ponto de vista do** | estudante de graduação da UnB |
| **no contexto** | das tarefas T1 a T6 e do planejamento do fluxo de disciplinas (OP-07), na versão v4.15.10.115 em uso no 2º semestre letivo de 2026 |

**Justificativa:** Adequação Funcional ficou em segundo lugar na matriz Impacto x Risco (P = 20). O estudante depende do SIGAA para tarefas sem alternativa institucional, e a existência de ferramentas comunitárias para planejar o fluxo (OP-07) indica lacunas de completude. G1 verifica se as funções necessárias existem, se produzem informações corretas e se bastam para a tarefa sem recurso a ferramentas externas.

## G2 - Capacidade de Interação (Usabilidade)

*Tabela 2 - Objetivo de medição G2 - Capacidade de Interação.*

| Elemento | Definição |
| -------- | --------- |
| **Analisar** | a interface web do portal do discente do SIGAA/UnB |
| **com o propósito de** | avaliar, a fim de identificar pontos fracos |
| **com respeito à** | capacidade de interação (reconhecimento de adequação, apreensibilidade, operabilidade, proteção contra erros do usuário, inclusividade e autodescritividade), complementada pela satisfação (qualidade em uso) |
| **do ponto de vista do** | estudante de graduação da UnB, com atenção a calouros e a estudantes com deficiência |
| **no contexto** | da execução das tarefas T1 a T6 em computador, na versão v4.15.10.115 em uso no 2º semestre letivo de 2026 |

**Justificativa:** Capacidade de Interação é a característica de maior prioridade na Fase 1 (P = 25) e a que reúne mais observações preliminares (OP-01 a OP-06). G2 verifica se o estudante localiza as funções, aprende a usá-las sem ajuda, conclui as tarefas com esforço razoável, recupera-se de erros, encontra barreiras de acessibilidade e compreende as informações sem legenda externa.

## G3 - Flexibilidade (Portabilidade)

*Tabela 3 - Objetivo de medição G3 - Flexibilidade.*

| Elemento | Definição |
| -------- | --------- |
| **Analisar** | a interface web do portal do discente do SIGAA/UnB |
| **com o propósito de** | avaliar, a fim de identificar pontos fracos |
| **com respeito à** | flexibilidade (adaptabilidade) |
| **do ponto de vista do** | estudante de graduação da UnB, com atenção ao estudante que acessa o sistema apenas pelo celular |
| **no contexto** | do acesso pelos navegadores Chrome, Firefox, Edge e Safari, em computador, tablet e celular, com interação por mouse e por toque |

**Justificativa:** Flexibilidade obteve P = 16 na Fase 1. O layout de largura fixa e os menus acionados pela passagem do ponteiro (OP-02 e OP-03) podem impedir o estudante que só usa o celular de concluir suas tarefas. G3 verifica se o SIGAA funciona da mesma forma nos navegadores, tamanhos de tela e modos de interação considerados no escopo.

## G4 - Eficiência de Desempenho

*Tabela 4 - Objetivo de medição G4 - Eficiência de Desempenho.*

| Elemento | Definição |
| -------- | --------- |
| **Analisar** | as páginas do portal do discente do SIGAA/UnB usadas nas tarefas T1 a T6 |
| **com o propósito de** | avaliar, a fim de identificar pontos fracos |
| **com respeito à** | eficiência de desempenho (comportamento temporal e utilização de recursos no cliente) |
| **do ponto de vista do** | estudante de graduação da UnB, com atenção a quem acessa por rede móvel |
| **no contexto** | da medição do lado do cliente, em rede comum e em rede móvel simulada, na versão v4.15.10.115 em uso no 2º semestre letivo de 2026 |

**Justificativa:** Eficiência de Desempenho obteve P = 16 na Fase 1. A lentidão atrasa todas as tarefas e pesa mais para quem usa rede móvel, e a interface gera páginas com muitos elementos e requisições. G4 verifica o tempo de carregamento das páginas e o volume de dados que o navegador precisa baixar. A medição é feita apenas no cliente, sem testes de carga, conforme a restrição registrada no [escopo](../fase-1/escopo.md#4-o-que-fica-fora-do-escopo).

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
