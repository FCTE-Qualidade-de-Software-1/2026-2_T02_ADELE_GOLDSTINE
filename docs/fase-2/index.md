# Fase 2 - Especificação da Avaliação

Esta fase corresponde à segunda atividade do processo de avaliação de produto da **ISO/IEC 25040** [2], na qual a avaliação é especificada: definem-se os objetivos de medição, as questões que eles levantam, as métricas que respondem a essas questões e os critérios usados para julgar os resultados.

Para isso, a equipe adotou o método **Goal–Question–Metric (GQM)** [1], que organiza a medição em três níveis (Tabela 1).

*Tabela 1 - Níveis do método GQM.*

| Nível | Elemento GQM | O que define |
| ----- | ------------ | ------------ |
| Conceitual | Objetivo (G) | O que se quer avaliar, com qual propósito, sob qual ponto de vista e em qual contexto |
| Operacional | Questão (Q) | Como o objetivo será caracterizado, por meio de perguntas sobre o foco de qualidade |
| Quantitativo | Métrica (M) | Quais dados objetivos respondem a cada questão |

Cada questão é acompanhada de uma **hipótese** (resultado esperado pela equipe antes da medição) e cada métrica possui **níveis de pontuação** que permitem julgar o resultado.

## 2.1 Rastreabilidade com a Fase 1

Todas as decisões desta fase derivam da [Fase 1](../fase-1/index.md). A Tabela 2 mostra onde cada decisão da Fase 1 é usada.

*Tabela 2 - Rastreabilidade entre a Fase 1 e a Fase 2.*

| Decisão da Fase 1 | Como é usada na Fase 2 |
| ----------------- | ---------------------- |
| Propósito: transformar percepções em evidências mensuráveis sobre os pontos fracos do SIGAA nas tarefas mais frequentes do estudante ([Propósito](../fase-1/proposito-stakeholders.md#1-proposito-da-avaliacao)) | Propósito dos quatro objetivos; níveis de pontuação definidos antes da coleta |
| Decisões apoiadas, sobretudo a priorização de telas e fluxos pela STI/UnB ([Propósito](../fase-1/proposito-stakeholders.md#13-como-os-resultados-serao-usados)) | Resultados apresentados por tarefa (regra 3 de [Níveis de Pontuação](niveis-pontuacao.md#regras-complementares)); investimento em interface responsiva apoiado por G3; otimização de páginas apoiada por M18 e M19 |
| Perfis de usuários: calouro, veterano, formando, estudante que só usa o celular e estudante com deficiência ([Partes Interessadas](../fase-1/proposito-stakeholders.md#22-perfis-de-usuarios-considerados)) | Ponto de vista dos objetivos; análise por perfil em M5, M6, M7 e M11; inclusividade em Q8; uso no celular em Q12 |
| Software avaliado: SIGAA/UnB, versão v4.15.10.115, e observações preliminares OP-01 a OP-08 ([Software Avaliado](../fase-1/software-avaliado.md#4-observacoes-preliminares-da-interface)) | Contexto dos objetivos; OP-01 em M11, OP-02 e OP-03 em M14, OP-04 em M4, OP-05 em M6 e M7, OP-06 em M8, OP-07 em M1 e M3; OP-08 (recurso A+/A-, ponto positivo) não gera métrica própria, e a ampliação é verificada pelo critério (c) de M10 |
| Modelo de qualidade: ISO/IEC 25010:2023 [3] adaptado, com as subcaracterísticas mantidas ([Modelo de Qualidade](../fase-1/modelo-qualidade.md#2-adaptacoes-ao-contexto-do-sigaa)) | Uma ou mais questões para cada subcaracterística mantida (Q1 a Q9 e Q11 a Q14) |
| Características priorizadas: Capacidade de Interação (Usabilidade), Adequação Funcional, Eficiência de Desempenho e Flexibilidade (Portabilidade) ([Características](../fase-1/caracteristicas.md#3-caracteristicas-selecionadas)) | Objetivos G1 a G4 |
| Escopo: tarefas T1 a T6 e ambientes de execução ([Escopo](../fase-1/escopo.md#2-o-que-sera-avaliado-agora)) | Tarefas usadas em todas as medições (seção 2.2); navegadores, telas e rede em G3 e G4 |
| Profundidade e técnicas por característica ([Escopo](../fase-1/escopo.md#3-profundidade-por-caracteristica)) | Instrumentos de coleta das métricas (seção 2.3) |
| Rigor intermediário: critérios antes da coleta, medições repetidas e mais de um avaliador ([Escopo](../fase-1/escopo.md#7-rigor-da-avaliacao)) | Dois avaliadores em M1, M2 e M10; cinco execuções em M16 a M19 |
| Relações esperadas entre as características ([Características](../fase-1/caracteristicas.md#5-relacoes-esperadas-entre-as-caracteristicas)) | Métricas que verificam cada relação (Tabela 5) |

**Ponto de vista:** em todos os objetivos, o ponto de vista adotado é o do **estudante de graduação da UnB**, com atenção aos perfis definidos na Fase 1. Os principais usuários dos resultados são a STI/UnB, o DEG e as coordenações de curso, que precisam de evidências objetivas e resultados por tarefa para priorizar melhorias.

## 2.2 Tarefas

As métricas de Capacidade de Interação, Flexibilidade e Eficiência de Desempenho são coletadas sobre as tarefas representativas definidas na Fase 1 (Tabela 3). Usar as mesmas tarefas em todas as medições permite comparar os resultados entre características. O caminho no sistema e a criticidade de cada tarefa estão na Tabela 1 de [Escopo e Rigor](../fase-1/escopo.md#21-tarefas-representativas).

*Tabela 3 - Tarefas representativas usadas nas medições.*

| ID | Tarefa |
| -- | ------ |
| T1 | Consultar as notas de uma disciplina do semestre |
| T2 | Identificar dia, horário e local de uma turma do semestre |
| T3 | Emitir atestado de matrícula ou histórico escolar |
| T4 | Verificar índices acadêmicos e carga horária pendente para a formatura |
| T5 | Acessar um material publicado pelo professor na Turma Virtual |
| T6 | Consultar o calendário acadêmico (ex.: prazo de trancamento) |

## 2.3 Instrumentos de coleta

A Tabela 4 relaciona as técnicas previstas na Fase 1 às métricas que cada uma produz.

*Tabela 4 - Instrumentos de coleta e métricas produzidas.*

| Instrumento | Técnica prevista na Fase 1 | Métricas |
| ----------- | -------------------------- | -------- |
| Teste com usuários estudantes sobre T1 a T6, gravado mediante consentimento | Testes com usuários (Capacidade de Interação) | M4, M5, M6, M7, M8, M11, M12 |
| Inspeção por dois avaliadores com roteiro | Roteiro de verificação de funções e conferência de dados (Adequação Funcional); verificação manual de acessibilidade | M1, M2, M10 |
| Execução das tarefas em matriz de navegadores e telas | Matriz de navegadores e tamanhos de tela (Flexibilidade) | M13, M14, M15 |
| Ferramentas automáticas (WAVE e Lighthouse) | Verificação automatizada de acessibilidade; medição do lado do cliente (Eficiência de Desempenho) | M9, M16, M17, M18, M19 |
| Questionário online anônimo | Complementa o roteiro de verificação de funções (Adequação Funcional); motivado pelo indício OP-07, sem técnica correspondente na Tabela 3 do escopo | M3 |

**Inspeção heurística:** prevista na Fase 1 para Capacidade de Interação, ela é usada como evidência qualitativa para interpretar Q4 (reconhecimento de adequação) e Q9 (autodescritividade) na Fase 4. Ela não gera métrica própria porque a severidade atribuída a cada problema depende do julgamento do avaliador, e as métricas desta fase precisam produzir o mesmo valor quando aplicadas por avaliadores diferentes.

## 2.4 Relações entre as características

A Fase 1 registrou quatro relações esperadas entre as características selecionadas, a serem confirmadas ou refutadas na Fase 4. A Tabela 5 indica as métricas que fornecem a evidência de cada relação.

*Tabela 5 - Métricas que verificam as relações esperadas entre as características.*

| Relação esperada (Fase 1) | Evidência na Fase 2 |
| ------------------------- | ------------------- |
| Flexibilidade → Capacidade de Interação | M15 (tempo no celular em relação ao computador) e M14 (páginas adaptadas), por tarefa |
| Eficiência de Desempenho → Capacidade de Interação | Correlação, por tarefa, entre M16 (tempo de carregamento) e M6 (tempo relativo de execução) |
| Capacidade de Interação → Adequação Funcional | Ocorrências, registradas nas sessões de teste (M5), em que o participante declara que uma função não existe quando ela consta na verificação de M1 |
| Eficiência de Desempenho → Flexibilidade | Comparação entre M17 (rede móvel simulada) e M16 (rede comum) |

## 2.5 Estrutura da especificação

- [Objetivos](objetivos.md): objetivos de medição G1 a G4, no template GQM.
- [Questões](questoes.md): questões Q1 a Q14 e a subcaracterística associada a cada uma.
- [Hipóteses](hipoteses.md): resultado esperado para cada questão (H1 a H14).
- [Métricas](metricas.md): definição, cálculo, fonte de dados, coleta e interpretação das métricas M1 a M19, com base na ISO/IEC 25023 [4] quando há medida equivalente.
- [Níveis de Pontuação](niveis-pontuacao.md): faixas de cada métrica e critérios de julgamento por característica.
- [Gráfico GQM](grafico-gqm.md): diagramas da hierarquia Objetivo, Questões e Métricas (Figuras 1 a 5).

## Referências

[1] BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994.

[2] ISO/IEC 25040:2024. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality evaluation framework*.

[3] ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

[4] ISO/IEC 25023:2016. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 17/10/2026 | Visão geral da Fase 2, rastreabilidade com a Fase 1 e tarefas-alvo | Felipe Campêlo |
| 1.2 | 18/10/2026 | Numeração e legendas de tabelas; ajustes de rastreabilidade com a Fase 1; citação das referências | Felipe Campêlo |
| 2.0 | 18/10/2026 | Alinhamento à Fase 1 reestruturada: ISO/IEC 25010:2023, quatro objetivos, tarefas T1 a T6, instrumentos de coleta e relações entre características | Felipe Campêlo |
