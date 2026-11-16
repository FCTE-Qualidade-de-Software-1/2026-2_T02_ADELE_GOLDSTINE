# Eficiência de Desempenho: dados complementares

!!! note "Fora do julgamento"
    Eficiência de Desempenho foi priorizada na Fase 1 (P = 16), mas a equipe a retirou da especificação na Fase 2 ([Objetivos](../fase-2/objetivos.md)). Por isso, os dados desta página **não têm questão GQM, hipótese nem nível de pontuação e não alteram o julgamento de nenhuma característica**. Eles são registrados porque vieram da mesma execução instrumentada de [Flexibilidade](flexibilidade.md) e porque dão evidência objetiva sobre a lentidão relatada pelos estudantes, que o artigo da Entrega 1 registrou como lacuna, e sobre duas relações levantadas na [Fase 1](../fase-1/caracteristicas.md#5-relacoes-esperadas-entre-as-caracteristicas).

## 1. O que foi medido

A ISO/IEC 25010:2023 divide Eficiência de Desempenho em comportamento temporal, utilização de recursos e capacidade [1]. A Fase 1 descartou a capacidade, porque exigiria testes de carga, intrusivos em produção ([Modelo de Qualidade](../fase-1/modelo-qualidade.md#2-adaptacoes-ao-contexto-do-sigaa)). Esta página mede as outras duas **do lado do cliente**, como previa a [Tabela 3 do escopo](../fase-1/escopo.md#3-profundidade-por-caracteristica), em quatro dimensões: **rapidez** (quanto o estudante espera), **responsividade** (se a página responde logo à interação), **estabilidade visual** (se o conteúdo fica parado depois de aparecer) e **fluidez** (se a rolagem é suave). Todas as medidas vêm de APIs padronizadas do navegador, e não de cronômetro.

*Tabela 1 - Medidas registradas.*

| Dimensão | Medida | Subcaracterística (ISO/IEC 25010) | Referência (ISO/IEC 25023) [2] | Como é obtida |
| -------- | ------ | --------------------------------- | ------------------------------ | ------------- |
| Rapidez | Espera na tarefa: soma do tempo de carregamento (`loadEventEnd`) de todas as páginas do caminho | Comportamento temporal | Tempo médio de execução (PTb-3-G), parcela do sistema | Navigation Timing [3] |
| Rapidez | Tempo de resposta do servidor (TTFB, `responseStart`) | Comportamento temporal | Tempo médio de resposta (PTb-1-G) | Navigation Timing |
| Rapidez | Primeiro conteúdo pintado (FCP) e maior conteúdo pintado (LCP) | Comportamento temporal | Tempo médio de resposta (PTb-1-G), do ponto de vista do que o usuário vê | Paint Timing e Largest Contentful Paint |
| Responsividade | Tempo de abertura do menu Ensino (do ponteiro ou toque até o submenu visível) | Comportamento temporal | Tempo médio de resposta (PTb-1-G) de uma interação | Relógio do *script*, com espera ativa pelo submenu |
| Responsividade | Tarefas longas (> 50 ms) da *thread* principal e *Total Blocking Time* (TBT, soma do que passa de 50 ms em cada tarefa longa) | Utilização de recursos (processamento no cliente) | Utilização média do processador (PRu-1-G), lado do cliente | Long Tasks API |
| Estabilidade | *Cumulative Layout Shift* (CLS): quanto o conteúdo se desloca depois de aparecer | Comportamento temporal (percepção) | Sem medida equivalente; referência dos Core Web Vitals [4] | Layout Instability API |
| Fluidez | Quadros por segundo e quadros acima de 50 ms ao rolar a página do topo ao fim | Utilização de recursos (renderização) | Sem medida equivalente | `requestAnimationFrame` durante rolagem programada |
| Recursos | Requisições, bytes transferidos e elementos no DOM | Utilização de recursos | Utilização da largura de banda (PRu-4-S) | Resource Timing e DOM |

*Fonte: elaboração da equipe.*

A espera na tarefa **não** é o tempo que o estudante leva para concluí-la (esse é M6, medido nas sessões): é só a parcela em que ele espera o sistema, sem leitura nem decisão.

## 2. Procedimento

- **Instrumento:** o *script* de [Flexibilidade](flexibilidade.md#2-metodo-execucao-instrumentada) (`coleta/sigaa_coleta.py desempenho`), no Google Chrome 146 estável, com as mesmas regras éticas e de proteção de dados. Os observadores de tarefas longas, de deslocamento de *layout* e de eventos são instalados em cada página **antes** dos *scripts* do SIGAA, para não perder nada do carregamento.
- **Tarefas e caminho:** T1 a T6, a partir da página inicial do Portal do Discente, pelo caminho principal da Fase 1. T2 mede o próprio portal; T6 tem duas páginas (lista de calendários e calendário 2026.2); T5 tem a página da Turma Virtual e o *download* do PDF, registrado à parte.
- **Cache desativado** em todas as execuções, para que cada medida represente o primeiro acesso e as repetições sejam comparáveis.
- **Repetições:** cinco no computador e três no celular em 4G, intercaladas (T1 a T6, depois T1 a T6 de novo), com 3 s de pausa. O resumo usa a **mediana**, que não é distorcida por uma execução isolada, e o **percentil 75** (P75, método *nearest-rank*), a estatística que o Google usa para classificar páginas [4].
- **Espera entre páginas:** antes de sair de cada página, o *script* espera a rede ficar ociosa (até 90 s), para não cancelar requisições pendentes, e registra o motivo de cada requisição que falhar.
- **Validade:** só entra nas estatísticas a execução sem erro, com os textos que comprovam a conclusão da tarefa e sem falha de requisição do SIGAA (cancelamentos do próprio navegador não contam). Se uma falha ocorre, o *script* repete a tarefa até três vezes.

*Tabela 2 - Cenários de medição.*

| Cenário | Tela | Rede | CPU | Por que |
| ------- | ---- | ---- | --- | ------- |
| Computador | 1366 × 768 px | Banda larga doméstica, sem limitação | Sem limitação | Situação das sessões do teste com usuários |
| Celular em 4G | 360 × 800 px, emulação de celular | Perfil de rede móvel do Lighthouse [5]: latência de 562,5 ms por requisição, 1,47 Mbit/s de *download* e 675 kbit/s de *upload* | 4 vezes mais lenta | Estudante que depende do celular e da rede móvel, perfil da [Fase 1](../fase-1/proposito-stakeholders.md#22-perfis-de-usuarios-considerados) |

*Fonte: elaboração da equipe.*

## 3. Referências de leitura

Como não há níveis de pontuação, os valores são lidos contra referências externas, sem julgamento:

- **Limites de Nielsen [6]:** até 0,1 s, a resposta parece instantânea; até 1 s, o fluxo de pensamento não é interrompido; até 10 s, a atenção se mantém na tarefa.
- **Core Web Vitals [4], no P75:** LCP bom até 2,5 s e ruim acima de 4,0 s; CLS bom até 0,1 e ruim acima de 0,25. Referências complementares do mesmo guia: TTFB bom até 0,8 s e FCP bom até 1,8 s.
- **Tarefa longa:** acima de 50 ms, a *thread* principal fica bloqueada a ponto de a resposta a um clique ou toque poder atrasar perceptivelmente; 60 quadros por segundo (cerca de 16,7 ms por quadro) é a referência de rolagem suave.

## 4. Resultados

### 4.1 Validade

**46 das 48 execuções são válidas.** As duas descartadas são de T5 no celular: em ambas, a rede local do computador de coleta oscilou durante o carregamento (`net::ERR_NETWORK_CHANGED`), e em uma delas o PDF não chegou a ser baixado. O mesmo motivo explica todas as nove repetições automáticas: nenhuma falha registrada veio do servidor do SIGAA.

### 4.2 Rapidez

*Tabela 3 - Rapidez no computador, rede sem limitação (Chrome 146, cache desativado, 15/11/2026).*

| Tarefa | Válidas | Espera na tarefa: mediana (s) | P75 (s) | Mín.-máx. (s) | TTFB (s) | FCP (s) | LCP mediano (s) | LCP P75 (s) |
| ------ | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| T1 Notas | 5 de 5 | 1,11 | 1,17 | 1,10-1,21 | 0,93 | 1,08 | 1,10 | 1,14 |
| T2 Portal (turmas) | 5 de 5 | 1,03 | 1,22 | 0,91-1,27 | 0,35 | 0,79 | 0,96 | 1,16 |
| T3 Atestado | 5 de 5 | 0,62 | 0,65 | 0,57-1,03 | 0,22 | 0,55 | 0,57 | 0,58 |
| T4 Índices | 5 de 5 | 1,62 | 1,71 | 1,31-2,00 | 0,98 | 1,60 | 1,62 | 1,67 |
| T5 Turma Virtual | 5 de 5 | 2,13 | 2,27 | 1,94-2,38 | 0,55 | 1,80 | 1,87 | 1,89 |
| T6 Calendário (2 páginas) | 5 de 5 | 1,59 | 1,76 | 1,30-1,89 | 0,10 | 0,72 | 0,74 | 0,74 |

*Fonte: `dados/consolidados/desempenho.csv`. TTFB, FCP e LCP referem-se à página final da tarefa; a espera na tarefa soma todas as páginas do caminho. Em T5, o* download *do PDF levou mediana de 0,27 s e não está somado.*

*Tabela 4 - Rapidez no celular em 4G simulado (360 px, rede e CPU limitadas).*

| Tarefa | Válidas | Espera na tarefa: mediana (s) | P75 (s) | Mín.-máx. (s) | TTFB (s) | FCP (s) | LCP mediano (s) | LCP P75 (s) |
| ------ | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| T1 Notas | 3 de 3 | 2,81 | 3,01 | 2,63-3,01 | 0,89 | 2,02 | 2,03 | 2,13 |
| T2 Portal (turmas) | 3 de 3 | 8,55 | 8,57 | 8,54-8,57 | 0,32 | 5,63 | 6,91 | 6,95 |
| T3 Atestado | 3 de 3 | 3,55 | 3,68 | 3,45-3,68 | 0,32 | 2,88 | 2,88 | 3,01 |
| T4 Índices | 3 de 3 | 6,51 | 6,52 | 6,32-6,52 | 0,82 | 5,40 | 5,42 | 5,45 |
| T5 Turma Virtual | 1 de 3 | 19,04 | 19,04 | 19,04-19,04 | 0,52 | 13,25 | 13,66 | 13,66 |
| T6 Calendário (2 páginas) | 3 de 3 | 10,13 | 10,43 | 10,00-10,43 | 0,10 | 3,87 | 3,90 | 3,92 |

*Fonte: idem. Em T5, só uma das três execuções é válida (seção 4.1); o valor deve ser lido com essa ressalva.*

### 4.3 Responsividade, estabilidade, fluidez e recursos

*Tabela 5 - Responsividade, estabilidade, fluidez e recursos (medianas).*

| Tarefa | Cenário | Abertura do menu (ms) | Tarefas longas | TBT (ms) | Maior tarefa longa (ms) | CLS | Rolagem (fps) | Quadro P95 (ms) | Quadros > 50 ms | Requisições | Transferido (KB) | Elementos no DOM |
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| T1 Notas | Computador | 32 | 0 | 0 | 0 | 0,000 | 60 | 16,9 | 0 | 17 | 134 | 588 |
| T1 Notas | Celular 4G | 58 | 1 | 42 | 122 | 0,012 | 60 | 17,3 | 0 | 17 | 134 | 588 |
| T2 Portal (turmas) | Computador | - | 0 | 0 | 0 | 0,134 | 60 | 16,9 | 0 | 61 | 566 | 1323 |
| T2 Portal (turmas) | Celular 4G | - | 1 | 49 | 138 | 0,051 | 60 | 17,3 | 0 | 61 | 567 | 1327 |
| T3 Atestado | Computador | 57 | 0 | 0 | 0 | 0,000 | 60 | 16,9 | 0 | 21 | 204 | 387 |
| T3 Atestado | Celular 4G | 68 | 1 | 62 | 144 | 0,000 | 60 | 17,3 | 0 | 21 | 204 | 387 |
| T4 Índices | Computador | 56 | 0 | 0 | 0 | 0,000 | 60 | 16,9 | 0 | 36 | 504 | 266 |
| T4 Índices | Celular 4G | 73 | 1 | 57 | 169 | 0,000 | 60 | 17,2 | 0 | 36 | 504 | 266 |
| T5 Turma Virtual | Computador | - | 0 | 0 | 0 | 1,053 | 60 | 17,3 | 0 | 131 | 1955 | 1069 |
| T5 Turma Virtual | Celular 4G | - | 2 | 99 | 117 | 0,012 | 60 | 17,2 | 0 | 131 | 1955 | 1074 |
| T6 Calendário (2 páginas) | Computador | 39 | 0 | 0 | 50 | 0,000 | 60 | 17,0 | 0 | 35 | 398 | 244 |
| T6 Calendário (2 páginas) | Celular 4G | 78 | 1 | 74 | 261 | 0,000 | 60 | 17,3 | 0 | 35 | 399 | 248 |

*Fonte: idem. A abertura do menu só se aplica às tarefas que passam pelo menu Ensino. TBT e tarefas longas somam as páginas do caminho; o CLS é o da página final; a rolagem é feita na página final.*

## 5. O que os dados revelam

**1. No computador, o SIGAA é rápido e fluido fora do horário de pico.** Todas as tarefas esperam de 0,62 a 2,13 s (mediana) pelo sistema, o LCP no P75 fica abaixo de 1,9 s em todas (faixa "boa"), não há tarefas longas (TBT = 0), o menu abre em 32 a 57 ms (abaixo do limite de 0,1 s em que a resposta parece instantânea) e a rolagem roda a 60 quadros por segundo, sem nenhum quadro travado. Esses dados **não confirmam a lentidão relatada pelos estudantes**, ao menos no horário medido; a explicação mais provável para os relatos são os picos de acesso, fora desta janela (seção 6).

**2. O servidor é o gargalo nas páginas que calculam dados do estudante.** O TTFB do relatório de notas (T1, 0,93 s) e dos índices (T4, 0,98 s) passa do limite "bom" de 0,8 s e é cerca de dez vezes o do calendário (T6, 0,10 s), uma página estática. Como TTFB mede o tempo até o primeiro byte, essa diferença é do processamento no servidor, e não do navegador nem do tamanho da página. Em T1 e T4, o servidor responde por mais da metade da espera total.

**3. A Turma Virtual "pula" depois de carregar.** O CLS da página da Turma Virtual no computador ficou entre 0,88 e 1,07 nas cinco execuções (mediana 1,05), **quatro vezes o limite "ruim" de 0,25**. Na prática, depois que o conteúdo aparece, os painéis da página se reorganizam e o conteúdo se desloca: um estudante que tente clicar logo no material pode acertar outro item. O portal (T2) também passa do limite "bom" (CLS de 0,13). No celular, o deslocamento quase não aparece (0,01), porque, com a rede lenta, a página se reorganiza antes de ser pintada.

**4. No celular em rede móvel, a espera passa dos limites de atenção.** Com a mesma página e a rede 4G simulada, o portal leva 8,55 s, os índices 6,51 s e a Turma Virtual 19,04 s; o LCP no P75 fica na faixa "ruim" (acima de 4 s) em T2, T4 e T5. A Turma Virtual é o caso extremo: 131 requisições e cerca de 1,9 MB transferidos (de 3 a 15 vezes as demais páginas). Só para transferir esse volume a 1,47 Mbit/s são necessários, no mínimo, **1,9 MB × 8 ÷ 1,47 Mbit/s ≈ 10,9 s**, e a medida (19,04 s) confirma que a página passa do limite de 10 s em que o usuário perde a atenção. No celular aparecem também as primeiras tarefas longas (até 261 ms, no calendário), embora o TBT fique abaixo de 100 ms em todas as páginas.

**5. O caminho tem passos que custam tempo sem trazer informação.** Em T6, a primeira página é a lista de todos os calendários desde 2000 (35 requisições), e o estudante precisa de uma segunda página para ver o semestre atual: no celular, a tarefa espera 10,13 s, e cerca de metade disso é a lista.

**Relação com as outras características.** A Fase 1 previa que o peso das páginas penalizaria mais o acesso em rede móvel (**Desempenho → Flexibilidade**). Os dados sustentam essa relação: as mesmas páginas que esperam de 0,62 a 2,13 s no computador esperam de 2,81 a 19,04 s no celular em 4G, e, exceto em T6, que tem duas páginas, a ordem acompanha o volume transferido. Somada ao resultado de M14 (nenhuma página adaptada), ela mostra que o estudante que depende do celular é penalizado duas vezes: pela tela e pela rede. Já a relação **Desempenho → Capacidade de Interação** não pode ser verificada aqui: no computador, as páginas respondem rápido o bastante para que o tempo do estudante nas sessões (M6) seja dominado pela busca do caminho, e não pela espera.

## 6. Limitações

- **Um único ponto de rede e um único horário** (noite de 15/11/2026, das 23h24 às 23h45). Os estudantes relatam lentidão sobretudo em horários de pico, como a matrícula, fora desta janela. Os valores do computador tendem, portanto, a ser **otimistas**.
- **Rede móvel simulada.** A limitação aplica latência e banda fixas; uma rede 4G real varia mais. O perfil usado é o de referência do Lighthouse, o que permite comparar com outras medições publicadas.
- **Lado do cliente.** As medidas incluem rede e navegador e não isolam o processamento do servidor, conforme o limite do [escopo da Fase 1](../fase-1/escopo.md#5-limites-de-validade-dos-resultados); o TTFB é a melhor aproximação disponível.
- **Uma conta.** O tamanho de algumas páginas depende dos dados da conta (por exemplo, o relatório de notas cresce com o número de semestres cursados).
- **Uma rodada anterior foi descartada.** A primeira coleta (mesma noite) saía de cada página sem esperar a rede ficar ociosa e não registrava o motivo das falhas; no cenário 4G, não era possível separar falha real de requisição cancelada pela própria medição. O protocolo foi corrigido (seção 2) e a coleta refeita; só a segunda rodada está no repositório.

## Referências

[1] ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

[2] ISO/IEC 25023:2016. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality*.

[3] W3C. *Navigation Timing Level 2*. Disponível em: <https://www.w3.org/TR/navigation-timing-2/>. Acesso em: 15 nov. 2026.

[4] GOOGLE. *Web Vitals*. web.dev. Disponível em: <https://web.dev/articles/vitals>. Acesso em: 18 out. 2026.

[5] GOOGLE. *Introduction to Lighthouse*. Chrome for Developers. Disponível em: <https://developer.chrome.com/docs/lighthouse/overview>. Acesso em: 19 out. 2026.

[6] NIELSEN, J. *Usability Engineering*. San Francisco: Morgan Kaufmann, 1993.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 15/11/2026 | Medidas complementares de rapidez, responsividade, estabilidade visual e fluidez do lado do cliente, em dois cenários, com método, resultados, análise e limitações | [arthurlleite](https://github.com/arthurlleite) |
