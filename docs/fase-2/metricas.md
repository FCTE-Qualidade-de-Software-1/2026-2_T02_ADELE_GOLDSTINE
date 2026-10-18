# Métricas

As métricas representam o **nível quantitativo** do GQM. Para cada métrica são documentados a questão que ela responde, a definição, o procedimento de cálculo, a fonte dos dados, o procedimento de coleta e o critério de interpretação. Sempre que possível, as fórmulas seguem as medidas propostas na ISO/IEC 25023 [1]. As métricas obtidas na execução das tarefas pelos estudantes (conclusão, tempo e satisfação) também correspondem às medidas de eficácia, eficiência e satisfação da ISO/IEC 25022 [6].

As métricas foram escolhidas por serem **simples** (calculadas com contagens, razões ou medianas), **objetivas** (dois avaliadores seguindo o mesmo procedimento obtêm o mesmo valor) e **válidas** (cada uma mede diretamente o atributo perguntado na questão).

As faixas de julgamento de cada métrica estão na página [Níveis de Pontuação](niveis-pontuacao.md). As tarefas T1 a T6 estão na [visão geral da Fase 2](index.md#22-tarefas), e os instrumentos de coleta, na [seção 2.3](index.md#23-instrumentos-de-coleta) da mesma página. Toda medição registra data, horário, dispositivo, navegador e rede, conforme as premissas do [escopo da Fase 1](../fase-1/escopo.md#6-premissas-e-restricoes).

## Resumo

A Tabela 1 resume as métricas, e as Tabelas 2 a 21 detalham cada uma delas. A métrica auxiliar MA1 está na Tabela 22, e os artefatos de dados previstos, na Tabela 23.

*Tabela 1 - Resumo das métricas.*

| ID | Métrica | Questão | Fórmula | Melhor valor |
| -- | ------- | ------- | ------- | ------------ |
| M1 | Cobertura funcional | Q1 | X = 1 − A/B | 1 |
| M2 | Taxa de correção funcional | Q2 | X = 1 − A/B | 1 |
| M3 | Proporção de estudantes que usam ferramentas externas | Q3 | X = A/B | 0 |
| M4 | Acerto na primeira escolha de menu | Q4 | X = A/B | 1 |
| M5 | Taxa de conclusão de tarefas sem ajuda | Q5 | X = A/B | 1 |
| M6 | Tempo relativo de execução | Q6 | X = T<sub>p</sub> / T<sub>e</sub> | 1 |
| M7 | Desvio de caminho | Q6 | X = C<sub>p</sub> / C<sub>min</sub> | 1 |
| M8 | Taxa de recuperação de erros | Q7 | X = A/B | 1 |
| M9 | Erros automáticos de acessibilidade por página | Q8 | X = A/B | 0 |
| M10 | Critérios manuais de acessibilidade atendidos | Q8 | X = A/B | 1 |
| M11 | Interpretação correta sem legenda | Q9 | X = A/B | 1 |
| M12 | Pontuação SUS | Q10 | Escala SUS (0 a 100) | 100 |
| M13 | Compatibilidade entre navegadores | Q11 | X = A/B | 1 |
| M14 | Proporção de páginas adaptadas a telas pequenas e ao toque | Q12 | X = A/B | 1 |
| M15 | Tempo relativo no celular | Q12 | X = T<sub>m</sub> / T<sub>d</sub> | 1 |
| M16 | Tempo de carregamento em rede comum | Q13 | Mediana do LCP (s) | Menor possível |
| M17 | Tempo de carregamento em rede móvel simulada | Q13 | Mediana do LCP (s) | Menor possível |
| M18 | Peso transferido por página | Q14 | Mediana do total transferido (MB) | Menor possível |
| M19 | Requisições por página | Q14 | Mediana do número de requisições | Menor possível |
| M20 | Cobertura de tratamento de cenários de erro | Q7 | X = A/B | 1 |

Além delas, a métrica auxiliar **MA1** (taxa de declaração de função inexistente) é usada apenas para verificar a hipótese de relação HR3 e não recebe nível de pontuação (Tabela 22).

## Definições comuns

As definições abaixo valem para todas as métricas coletadas sobre as tarefas e são fixadas antes da coleta.

- **Caminho mais curto (caminho ótimo):** menor sequência de passos que conclui a tarefa a partir da página inicial do portal do discente, definida pela equipe por inspeção antes do teste. Caminhos alternativos válidos também são registrados e são usados para classificar a primeira escolha em M4.
- **Passo:** cada clique ou toque em link, botão, item de menu ou controle de seleção que muda o estado da interface, incluindo o envio de formulário. Rolagem, digitação dentro de um mesmo campo e cliques em áreas sem ação não contam como passo. Em M7, cada passo corresponde a um clique.
- **Ajuda:** qualquer intervenção do moderador, consulta a colega ou consulta a fonte externa (busca na internet, tutorial). Consultar a legenda do próprio sistema não é ajuda para M5; em M11, porém, abrir a legenda invalida a resposta, conforme a ficha da métrica.
- **Tarefa concluída:** o participante obtém a informação ou o documento pedido e o informa corretamente ao moderador, sem ajuda e em até 5 minutos, conforme os critérios de M5.

## G1 - Adequação Funcional

### M1 - Cobertura funcional

*Tabela 2 - Ficha da métrica M1 - Cobertura funcional.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q1 - O SIGAA oferece as funções de que o estudante precisa? |
| **Definição** | Proporção das funções necessárias ao estudante que estão implementadas no SIGAA. Baseada na medida de cobertura funcional da ISO/IEC 25023. |
| **Cálculo** | X = 1 − A/B, onde A = número de funções da lista de referência ausentes no SIGAA e B = número total de funções da lista de referência. |
| **Fonte dos dados** | Lista de referência de funções, montada a partir de (a) respostas à pergunta aberta sobre funções que o estudante sente falta no SIGAA, incluída no questionário de M3 (Tabela 4), (b) funções oferecidas por ferramentas comunitárias usadas pelos estudantes da UnB (OP-07) e (c) funções necessárias às tarefas T1 a T6. |
| **Procedimento de coleta** | 1. Consolidar a lista de referência, removendo duplicatas, e associar a cada tarefa as funções necessárias a ela (exemplo para T4: exibir o IRA; exibir a carga horária pendente por tipo de componente; listar os componentes obrigatórios pendentes). 2. Dois avaliadores verificam, de forma independente, se cada função existe no SIGAA, registrando a evidência (captura de tela e caminho de menus). 3. Divergências entre avaliadores são resolvidas por um terceiro membro. |
| **Interpretação** | Quanto mais próximo de 1, mais completo é o SIGAA em relação às necessidades dos estudantes. O resultado é calculado no geral e por tarefa, considerando as funções associadas a cada tarefa. Uma função que existe, mas não foi encontrada por um participante, não é contada como ausente; esse caso é registrado na métrica auxiliar MA1 (Tabela 22). |

### M2 - Taxa de correção funcional

*Tabela 3 - Ficha da métrica M2 - Taxa de correção funcional.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q2 - As informações exibidas pelo SIGAA estão corretas? |
| **Definição** | Proporção de verificações em que a informação exibida pelo SIGAA coincide com a fonte de referência. Baseada na medida de correção funcional da ISO/IEC 25023. |
| **Cálculo** | X = 1 − A/B, onde A = número de verificações com divergência e B = número total de verificações realizadas. |
| **Fonte dos dados** | (a) Fontes oficiais independentes do SIGAA: projeto pedagógico do curso (PPC) e calendário acadêmico publicado pela UnB. (b) Consistência interna entre documentos do próprio sistema, como o histórico emitido em T3 e os índices e a carga horária pendente exibidos em T4, conforme a técnica prevista no [escopo da Fase 1](../fase-1/escopo.md#3-profundidade-por-caracteristica). |
| **Procedimento de coleta** | 1. Para o curso de cada avaliador, comparar com o PPC a carga horária, os créditos e os pré-requisitos de todas as disciplinas obrigatórias dos quatro primeiros semestres do fluxo. 2. Comparar as datas exibidas em T6 com o calendário acadêmico publicado. 3. Conferir se os índices e a carga horária pendente de T4 são coerentes com o histórico emitido em T3. 4. Conferir se as notas e menções exibidas em T1 coincidem com as do histórico emitido em T3, e se o dia, o horário e o local da turma exibidos em T2 coincidem com os da Turma Virtual. 5. Cada atributo comparado conta como uma verificação; registrar o resultado em planilha (coincide ou diverge, com evidência), marcando os itens críticos: menção, IRA e carga horária pendente. 6. Um segundo avaliador repete as verificações de forma independente; divergências entre avaliadores são resolvidas por um terceiro membro. |
| **Interpretação** | Quanto mais próximo de 1, mais confiáveis são as informações. Qualquer divergência é registrada individualmente, por ter impacto direto na vida acadêmica. Uma divergência em item crítico (menção, IRA ou carga horária pendente) leva M2 ao nível Insatisfatório, qualquer que seja o valor de X (regra 2 de [Níveis de Pontuação](niveis-pontuacao.md#regra-2-itens-criticos-de-m2)). |

### M3 - Proporção de estudantes que usam ferramentas externas

*Tabela 4 - Ficha da métrica M3 - Proporção de estudantes que usam ferramentas externas.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q3 - As funções do SIGAA são suficientes para planejar o fluxo sem ferramentas externas? |
| **Definição** | Proporção de respondentes que declaram usar alguma ferramenta fora do SIGAA (site, aplicativo ou planilha) para planejar o fluxo ou a grade de horários. |
| **Cálculo** | X = A/B, onde A = número de respondentes que usam ferramenta externa e B = número total de respondentes válidos. |
| **Fonte dos dados** | Questionário online anônimo aplicado a estudantes de graduação da UnB. |
| **Procedimento de coleta** | 1. Divulgar o questionário em grupos de estudantes e centros acadêmicos. 2. Considerar válidas apenas respostas de estudantes de graduação ativos. 3. Registrar também quais ferramentas são usadas, por quê e quais funções o respondente sente falta no SIGAA, como insumo da lista de referência de M1 (Tabela 2). |
| **Interpretação** | Quanto menor o valor, mais adequadas são as funções do SIGAA para a tarefa de planejamento. |

## G2 - Capacidade de Interação (Usabilidade)

As métricas M4 a M8, M11 e M12 são coletadas em um **teste com usuários**: estudantes de graduação executam as tarefas T1 a T6 em computador, sem ajuda do moderador. As sessões são gravadas mediante consentimento, e os participantes são identificados apenas por código (P1, P2, ...) e por perfil (calouro, veterano ou formando), conforme os [perfis da Fase 1](../fase-1/proposito-stakeholders.md#22-perfis-de-usuarios-considerados). Durante as sessões, o moderador também registra as ocasiões em que o participante declara que uma função não existe (métrica auxiliar MA1, Tabela 22), evidência usada na relação entre Capacidade de Interação e Adequação Funcional (Tabela 5 da [visão geral](index.md#24-relacoes-entre-as-caracteristicas)).

### M4 - Acerto na primeira escolha de menu

*Tabela 5 - Ficha da métrica M4 - Acerto na primeira escolha de menu.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q4 - O estudante identifica onde está a função de que precisa? |
| **Definição** | Proporção de tentativas de tarefa em que o primeiro item de menu ou link escolhido pelo participante pertence ao caminho que leva à função. |
| **Cálculo** | X = A/B, onde A = número de tentativas com a primeira escolha correta e B = número total de tentativas (participantes × 6). |
| **Fonte dos dados** | Gravações das sessões do teste com usuários. |
| **Procedimento de coleta** | Antes do teste, a equipe registra, para cada tarefa, os itens de menu e links que pertencem a algum caminho válido. Nas gravações, um avaliador anota o primeiro item clicado em cada tentativa e o compara com essa lista. Passar o ponteiro sobre um menu sem clicar não conta como escolha. |
| **Interpretação** | Quanto mais próximo de 1, mais fácil é reconhecer onde está cada função. O resultado é analisado por tarefa, para identificar menus que confundem o estudante. |

### M5 - Taxa de conclusão de tarefas sem ajuda

*Tabela 6 - Ficha da métrica M5 - Taxa de conclusão de tarefas sem ajuda.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q5 - O estudante consegue concluir as tarefas sem ajuda? |
| **Definição** | Proporção de tentativas de tarefa concluídas corretamente, sem ajuda do moderador. Baseada na medida de conclusão de tarefas da ISO/IEC 25023. |
| **Cálculo** | X = A/B, onde A = número de tarefas concluídas corretamente e B = número total de tarefas tentadas (participantes × 6). |
| **Fonte dos dados** | Gravações das sessões e formulário de observação do moderador. |
| **Procedimento de coleta** | Para cada participante e tarefa, o moderador registra "concluída" ou "não concluída". A tarefa é considerada não concluída se o participante desistir, pedir ajuda, ultrapassar 5 minutos ou chegar a um resultado errado. Antes da sessão, o participante informa se já executou cada tarefa no SIGAA; no recorte de calouros, as tarefas já executadas antes do estudo são excluídas, para que o recorte meça o primeiro contato. |
| **Interpretação** | Quanto mais próximo de 1, mais fácil é aprender a usar o sistema. O resultado também é apresentado por perfil (calouro, veterano e formando), porque a apreensibilidade se manifesta sobretudo no primeiro contato. Diferença grande entre o recorte de calouros e o resultado geral indica dependência de experiência prévia. O recorte usa as mesmas faixas de M5 e não altera o nível da questão (regra 3 de [Níveis de Pontuação](niveis-pontuacao.md#regra-3-resultados-por-perfil-por-pagina-e-por-tarefa)). |

### M6 - Tempo relativo de execução

*Tabela 7 - Ficha da métrica M6 - Tempo relativo de execução.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q6 - A navegação permite concluir as tarefas sem esforço desnecessário em relação a um usuário experiente? |
| **Definição** | Razão entre o tempo médio dos participantes e o tempo de um usuário experiente para a mesma tarefa. |
| **Cálculo** | X = T<sub>p</sub> / T<sub>e</sub>, onde T<sub>p</sub> = tempo médio dos participantes que concluíram a tarefa e T<sub>e</sub> = tempo do especialista (membro da equipe que executa a tarefa pelo caminho mais curto, média de 3 execuções). O resultado final é a média das tarefas; uma tarefa que nenhum participante concluiu fica fora da média e é registrada à parte. |
| **Fonte dos dados** | Gravações das sessões, com marcação de início (leitura da tarefa concluída) e fim (resultado obtido). |
| **Procedimento de coleta** | Cronometrar cada tarefa a partir das gravações. Tarefas não concluídas não entram no cálculo de T<sub>p</sub>. |
| **Interpretação** | Quanto mais próximo de 1, mais fácil de operar é a interface para o estudante comum. |

### M7 - Desvio de caminho

*Tabela 8 - Ficha da métrica M7 - Desvio de caminho.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q6 - A navegação permite concluir as tarefas sem esforço desnecessário em relação a um usuário experiente? |
| **Definição** | Razão entre o número de cliques dos participantes e o número mínimo de cliques necessário para concluir a tarefa. |
| **Cálculo** | X = C<sub>p</sub> / C<sub>min</sub>, onde C<sub>p</sub> = média de cliques dos participantes que concluíram a tarefa e C<sub>min</sub> = número de cliques do caminho mais curto, definido pela equipe antes do teste. O resultado final é a média das tarefas; uma tarefa que nenhum participante concluiu fica fora da média e é registrada à parte. |
| **Fonte dos dados** | Gravações das sessões. |
| **Procedimento de coleta** | Contar os cliques em links, botões e menus a partir das gravações, desconsiderando cliques em áreas sem ação. Ao definir C<sub>min</sub>, dois avaliadores classificam também cada passo do caminho mais curto como necessário ou desnecessário. É **passo desnecessário** aquele que não fornece informação nova nem decisão ao estudante (ex.: tela de seleção com uma única opção, confirmação sem conteúdo). Essa classificação não altera o valor de M7 e é registrada como evidência do desenho dos fluxos. |
| **Interpretação** | Quanto mais próximo de 1, mais direta é a navegação. Valores altos indicam que o estudante se perde nos menus. Passos desnecessários no próprio caminho mais curto indicam esforço imposto pelo desenho das funções, que nenhum participante consegue evitar. |

### M8 - Taxa de recuperação de erros

*Tabela 9 - Ficha da métrica M8 - Taxa de recuperação de erros.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q7 - O sistema evita que o estudante perca o que já fez quando comete um erro ou quando a sessão expira? |
| **Definição** | Proporção dos erros ocorridos durante as tarefas dos quais o participante se recupera sem ajuda e sem precisar refazer passos já concluídos. |
| **Cálculo** | X = A/B, onde A = número de erros recuperados sem ajuda e sem retrabalho e B = número total de erros. Se nenhum erro ocorrer (B = 0), X = 1. |
| **Fonte dos dados** | Gravações das sessões do teste com usuários. |
| **Procedimento de coleta** | Conta como erro: ação em item errado que leva a uma página fora do caminho, envio de formulário com dado inválido, mensagem de erro do sistema e expiração da sessão durante a tarefa (OP-06). Para cada erro, um avaliador registra se o participante retornou ao ponto anterior sem ajuda e sem refazer passos. Passo já concluído é uma página do caminho correto já visitada ou um campo já preenchido; voltar pelo menu ou pelo botão Voltar sem repetir esses passos conta como recuperação. |
| **Interpretação** | Quanto mais próximo de 1, melhor o sistema protege o estudante das consequências dos próprios erros. |

### M20 - Cobertura de tratamento de cenários de erro

*Tabela 10 - Ficha da métrica M20 - Cobertura de tratamento de cenários de erro.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q7 - O sistema evita que o estudante perca o que já fez quando comete um erro ou quando a sessão expira? |
| **Definição** | Proporção dos cenários de erro previstos em que o sistema evita o erro ou o trata adequadamente. |
| **Cálculo** | X = A/B, onde A = número de cenários tratados e B = número de cenários verificados (6). |
| **Fonte dos dados** | Inspeção das páginas das tarefas T1 a T6, com o estudante autenticado, segundo um roteiro de cenários de erro definido antes da coleta. |
| **Procedimento de coleta** | Dois avaliadores provocam, de forma independente, os seis cenários: (C1) a sessão expira durante a tarefa (OP-06); (C2) uso do botão Voltar do navegador; (C3) recarregar a página após uma ação; (C4) abrir uma função em nova aba; (C5) acessar uma função indisponível no período do calendário; (C6) bloqueio de janela ao gerar documento em PDF. Um cenário é considerado **tratado** se o sistema o previne ou exibe mensagem que indica a causa e como continuar, sem obrigar o estudante a recomeçar a tarefa desde o login. Registrar a evidência de cada cenário (captura de tela e passos executados). Divergências entre avaliadores são resolvidas por um terceiro membro. Nenhum cenário altera dados acadêmicos. |
| **Interpretação** | Quanto mais próximo de 1, melhor o sistema protege o estudante. Complementa M8 com cenários que podem não ocorrer espontaneamente nas sessões do teste com usuários. |

### M9 - Erros automáticos de acessibilidade por página

*Tabela 11 - Ficha da métrica M9 - Erros automáticos de acessibilidade por página.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q8 - As páginas do escopo podem ser usadas por pessoas com deficiência? |
| **Definição** | Número médio de erros de acessibilidade por página, considerando os critérios de nível A e AA das WCAG 2.2 [4] verificáveis automaticamente. |
| **Cálculo** | X = A/B, onde A = total de erros detectados e B = número de páginas analisadas (a página final de cada tarefa T1 a T6). |
| **Fonte dos dados** | Relatórios da extensão WAVE (WebAIM) executada nas páginas do escopo. |
| **Procedimento de coleta** | Com o estudante autenticado, abrir cada página, executar a extensão e capturar o relatório. São contados apenas os itens classificados como erro, não os alertas. |
| **Interpretação** | Quanto menor, mais acessível é o sistema. A ferramenta detecta apenas parte dos problemas, então o valor representa um limite inferior; M10 complementa a verificação. |

### M10 - Critérios manuais de acessibilidade atendidos

*Tabela 12 - Ficha da métrica M10 - Critérios manuais de acessibilidade atendidos.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q8 - As páginas do escopo podem ser usadas por pessoas com deficiência? |
| **Definição** | Proporção de verificações manuais de acessibilidade atendidas nas páginas do escopo, com base em critérios das WCAG 2.2 [4] que as ferramentas automáticas não avaliam. |
| **Cálculo** | X = A/B, onde A = número de verificações atendidas e B = número de verificações realizadas (4 critérios × 6 páginas = 24). |
| **Fonte dos dados** | Inspeção manual das páginas finais de T1 a T6, com teclado, zoom do navegador e leitor de tela (NVDA no Windows ou VoiceOver no macOS). |
| **Procedimento de coleta** | Dois avaliadores verificam, de forma independente, em cada página: (a) todas as funções da tarefa são alcançáveis e acionáveis apenas pelo teclado; (b) o foco do teclado é sempre visível; (c) com zoom de 200%, o conteúdo continua legível e operável sem perda de informação; (d) o leitor de tela anuncia um nome compreensível para cada link, botão e campo usado na tarefa. Divergências são resolvidas por um terceiro membro. |
| **Interpretação** | Quanto mais próximo de 1, mais inclusivo é o sistema para estudantes que usam tecnologias assistivas ou recursos de ampliação. |

### M11 - Interpretação correta sem legenda

*Tabela 13 - Ficha da métrica M11 - Interpretação correta sem legenda.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q9 - O estudante compreende as informações exibidas sem consultar legenda ou ajuda externa? |
| **Definição** | Proporção de perguntas de compreensão respondidas corretamente pelo participante a partir da informação exibida, sem abrir legenda, ícone de ajuda ou fonte externa. |
| **Cálculo** | X = A/B, onde A = número de respostas corretas sem consulta e B = número total de perguntas (participantes × 3). |
| **Fonte dos dados** | Respostas dos participantes registradas nas sessões do teste com usuários. |
| **Procedimento de coleta** | Ao final de três tarefas, o moderador faz uma pergunta de compreensão: em T2, o dia e o horário da turma a partir do código exibido (OP-01); em T4, quantas horas faltam para a formatura; em T6, a data-limite de trancamento. A resposta conta como correta apenas se o participante não tiver aberto a legenda ou a ajuda. Se a tarefa não for concluída, a pergunta conta como incorreta. |
| **Interpretação** | Quanto mais próximo de 1, mais autodescritiva é a interface. O resultado por pergunta indica qual informação mais precisa de explicação na própria tela. |

### M12 - Pontuação SUS

*Tabela 14 - Ficha da métrica M12 - Pontuação SUS.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q10 - O estudante fica satisfeito ao usar o SIGAA nas tarefas de rotina? |
| **Definição** | Pontuação no questionário *System Usability Scale* (SUS) [2], instrumento padronizado de dez itens em escala Likert de 1 a 5. |
| **Cálculo** | Para itens ímpares, soma-se (resposta − 1); para itens pares, soma-se (5 − resposta). A soma é multiplicada por 2,5, gerando um valor de 0 a 100 por participante. O resultado é a média entre participantes. |
| **Fonte dos dados** | Questionário SUS em português, aplicado ao final de cada sessão do teste com usuários. |
| **Procedimento de coleta** | O participante responde ao questionário sozinho, logo após a última tarefa, sem interferência do moderador. |
| **Interpretação** | Quanto maior, maior a satisfação. A média de referência da literatura é 68 pontos [3]. |

## G3 - Flexibilidade (Portabilidade)

### M13 - Compatibilidade entre navegadores

*Tabela 15 - Ficha da métrica M13 - Compatibilidade entre navegadores.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q11 - As tarefas do escopo funcionam corretamente nos navegadores mais usados? |
| **Definição** | Proporção de combinações tarefa × navegador executadas sem falha. |
| **Cálculo** | X = A/B, onde A = número de combinações sem falha e B = número total de combinações (6 tarefas × 4 navegadores = 24). |
| **Fonte dos dados** | Execução das tarefas T1 a T6 pela equipe nas versões estáveis vigentes de Chrome, Firefox, Edge e Safari, em computador. |
| **Procedimento de coleta** | Para cada combinação, registrar "sem falha" ou "com falha" com captura de tela. Considera-se falha: elemento que não carrega, botão que não responde, layout quebrado que impede a leitura ou resultado diferente do obtido no Chrome. |
| **Interpretação** | Quanto mais próximo de 1, melhor o SIGAA se adapta a diferentes navegadores. |

### M14 - Proporção de páginas adaptadas a telas pequenas e ao toque

*Tabela 16 - Ficha da métrica M14 - Proporção de páginas adaptadas a telas pequenas e ao toque.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q12 - O SIGAA se adapta a telas de celular e tablet e à interação por toque? |
| **Definição** | Proporção de verificações página × tamanho de tela em que a página das tarefas é exibida e operada corretamente: sem rolagem horizontal, sem conteúdo cortado, com menus acionáveis por toque e com alvos de toque de dimensão mínima. |
| **Cálculo** | X = A/B, onde A = número de verificações adaptadas e B = número de verificações (6 páginas × 2 larguras = 12). |
| **Fonte dos dados** | Páginas finais de T1 a T6 abertas em celular real (cerca de 360 px de largura) e em tablet ou no modo de dispositivo do navegador com 768 px e emulação de toque, conforme os [ambientes da Fase 1](../fase-1/escopo.md#22-ambientes-de-execucao). |
| **Procedimento de coleta** | Uma página é considerada adaptada se atender aos cinco critérios: (a) não exige rolagem horizontal da página na largura verificada, sem zoom (no celular, 360 px; tabelas com rolagem própria dentro da página não contam como rolagem horizontal da página) (OP-03); (b) nenhum texto da tarefa tem fonte menor que 12 px, conferida no painel de ferramentas do desenvolvedor; (c) nenhum elemento fica sobreposto ou cortado; (d) todos os itens de menu usados na tarefa, nos menus horizontais do portal e no menu lateral da Turma Virtual, podem ser abertos e acionados apenas por toque (OP-02); (e) os controles da tarefa têm área de toque de pelo menos 24 × 24 px CSS, ou espaçamento equivalente, conforme o critério 2.5.8 da WCAG 2.2 [4], medida no inspetor de elementos. Registrar captura de tela de cada verificação e, quando a página não for adaptada, os critérios não atendidos. |
| **Interpretação** | Quanto mais próximo de 1, melhor a adaptação a dispositivos móveis. Os critérios não atendidos indicam se o problema é de layout (a a c) ou de interação por toque (d e e). |

### M15 - Tempo relativo no celular

*Tabela 17 - Ficha da métrica M15 - Tempo relativo no celular.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q12 - O SIGAA se adapta a telas de celular e tablet e à interação por toque? |
| **Definição** | Razão entre o tempo para executar as tarefas no celular e o tempo para executá-las no computador, pelo mesmo avaliador. |
| **Cálculo** | X = T<sub>m</sub> / T<sub>d</sub>, onde T<sub>m</sub> = soma dos tempos das tarefas T1 a T6 no celular e T<sub>d</sub> = soma dos tempos no computador. Média entre os avaliadores. Para o resultado por tarefa, calcula-se também a razão de cada tarefa. |
| **Fonte dos dados** | Gravação de tela das execuções em ambos os dispositivos. |
| **Procedimento de coleta** | Cada avaliador executa as tarefas primeiro no computador e depois no celular, pelo caminho mais curto, na mesma rede, cronometrando cada uma. |
| **Interpretação** | Quanto mais próximo de 1, mais equivalente é a experiência entre os dispositivos. Valores altos indicam que o uso no celular exige esforço adicional. |

## G4 - Eficiência de Desempenho

As métricas M16 a M19 são coletadas com o Lighthouse, no painel de ferramentas do desenvolvedor do Chrome, nas páginas finais de T1 a T6, com o estudante autenticado. Cada página é medida em cinco execuções, com o cache desativado, e o valor da página é a mediana das execuções. As medições são feitas em dias úteis, fora do período de matrícula, e cada uma registra data, horário, rede e as versões do Chrome e do Lighthouse.

O Lighthouse mede a página recarregando o endereço dela. Como parte das páginas do SIGAA é alcançada por envio de formulário, antes da coleta a equipe confirma, para cada tarefa, um endereço que abre a página final diretamente com o estudante autenticado. Quando isso não é possível, mede-se a última página da tarefa que tem endereço próprio, e a substituição é registrada junto ao resultado.

### M16 - Tempo de carregamento em rede comum

*Tabela 18 - Ficha da métrica M16 - Tempo de carregamento em rede comum.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q13 - As páginas das tarefas carregam em tempo aceitável, em rede comum e em rede móvel? |
| **Definição** | Tempo até a renderização do maior elemento visível da página (*Largest Contentful Paint*, LCP) [5], em rede comum. |
| **Cálculo** | X = média, entre as seis páginas, da mediana do LCP (em segundos) das cinco execuções de cada página. |
| **Fonte dos dados** | Relatórios do Lighthouse no modo *Desktop*, com a limitação de rede simulada padrão desse modo, em rede doméstica ou institucional. |
| **Procedimento de coleta** | Executar o Lighthouse cinco vezes por página e registrar o LCP de cada execução e as condições de medição. |
| **Interpretação** | Quanto menor, mais rápido o estudante vê o conteúdo principal da página. O resultado por página indica onde a otimização teria mais efeito. |

### M17 - Tempo de carregamento em rede móvel simulada

*Tabela 19 - Ficha da métrica M17 - Tempo de carregamento em rede móvel simulada.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q13 - As páginas das tarefas carregam em tempo aceitável, em rede comum e em rede móvel? |
| **Definição** | LCP [5] das páginas das tarefas em condições de rede móvel simulada. |
| **Cálculo** | X = média, entre as seis páginas, da mediana do LCP (em segundos) das cinco execuções de cada página. |
| **Fonte dos dados** | Relatórios do Lighthouse no modo *Mobile*, que simula rede móvel lenta e processador limitado. |
| **Procedimento de coleta** | Igual a M16, trocando o modo do Lighthouse para *Mobile* e mantendo a mesma rede física. |
| **Interpretação** | Quanto menor, melhor a experiência de quem acessa por rede móvel. A comparação com M16 verifica a relação entre Eficiência de Desempenho e Flexibilidade. De forma complementar, sem alterar o valor de M17 nem seu nível, o resultado pode ser reportado também pelo percentil 75 do LCP entre as páginas, forma usada pelas métricas Core Web Vitals [5], para que poucas páginas rápidas não escondam as lentas. |

### M18 - Peso transferido por página

*Tabela 20 - Ficha da métrica M18 - Peso transferido por página.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q14 - As páginas das tarefas usam os recursos do cliente de forma compatível com o acesso por rede móvel e plano de dados limitado? |
| **Definição** | Quantidade total de dados transferidos pela rede para carregar a página, incluindo HTML, folhas de estilo, scripts, imagens e fontes. |
| **Cálculo** | X = média, entre as seis páginas, da mediana do total transferido (em MB) nas cinco execuções de cada página. |
| **Fonte dos dados** | Auditoria de peso total da página (*total byte weight*) dos mesmos relatórios do Lighthouse de M16. |
| **Procedimento de coleta** | Registrar o valor da auditoria em cada execução de M16. |
| **Interpretação** | Quanto menor, menos dados o estudante consome, o que pesa mais para quem usa plano de dados móvel. |

### M19 - Requisições por página

*Tabela 21 - Ficha da métrica M19 - Requisições por página.*

| Item | Descrição |
| ---- | --------- |
| **Questão** | Q14 - As páginas das tarefas usam os recursos do cliente de forma compatível com o acesso por rede móvel e plano de dados limitado? |
| **Definição** | Número de requisições de rede feitas pelo navegador para carregar a página. |
| **Cálculo** | X = média, entre as seis páginas, da mediana do número de requisições nas cinco execuções de cada página. |
| **Fonte dos dados** | Auditoria de requisições de rede (*network requests*) dos mesmos relatórios do Lighthouse de M16. |
| **Procedimento de coleta** | Registrar o número de requisições em cada execução de M16. |
| **Interpretação** | Quanto menor, menos idas ao servidor são necessárias, o que reduz o tempo de carregamento em redes com alta latência. |

## Métrica auxiliar de relação

A métrica abaixo não responde a uma questão e não recebe nível de pontuação. Ela serve apenas para verificar a hipótese de relação HR3 (Capacidade de Interação → Adequação Funcional), descrita em [Hipóteses](hipoteses.md#hipoteses-de-relacao-entre-as-caracteristicas).

### MA1 - Taxa de declaração de função inexistente

*Tabela 22 - Ficha da métrica auxiliar MA1 - Taxa de declaração de função inexistente.*

| Item | Descrição |
| ---- | --------- |
| **Hipótese** | HR3 - Funções existentes, mas difíceis de localizar, são percebidas como ausentes |
| **Definição** | Proporção de tentativas de tarefa em que o participante afirma que a função pedida não existe no SIGAA, embora ela conste como existente na verificação de M1. |
| **Cálculo** | X = D/N, onde D = número de tentativas com essa declaração e N = número total de tentativas (participantes × 6). |
| **Fonte dos dados** | Gravações das sessões do teste com usuários e formulário de observação do moderador. |
| **Procedimento de coleta** | O moderador registra a declaração espontânea do participante ou a resposta à pergunta "o que você faria agora?" quando ele desiste da tarefa. A existência da função é conferida com a lista de referência verificada em M1. |
| **Interpretação** | Qualquer ocorrência indica que um problema de capacidade de interação está sendo percebido pelo estudante como problema de adequação funcional. |

## Artefatos de dados previstos

Para garantir a rastreabilidade exigida pela premissa 5 do roteiro, todos os dados ficarão no repositório, na pasta `dados/`, com os participantes identificados apenas por código (P1, P2, ...). A Tabela 23 lista os arquivos previstos e as métricas que cada um alimenta.

*Tabela 23 - Arquivos de dados previstos.*

| Arquivo | Conteúdo | Métricas |
| ------- | -------- | -------- |
| `dados/referencia/caminhos.csv` | Para cada tarefa: caminho mais curto, C<sub>min</sub>, caminhos alternativos válidos, itens de menu válidos para a primeira escolha, classificação de cada passo (necessário ou desnecessário) e tempos do especialista | M4, M6, M7 |
| `dados/brutos/questionario/respostas.csv` | Respostas anônimas do questionário online: uso de ferramenta externa, quais ferramentas e por quê, funções que o respondente sente falta | M3, M1 |
| `dados/brutos/testes-usuarios/sessoes.csv` | Uma linha por participante e tarefa: código, perfil, se já executou a tarefa antes, concluiu, houve ajuda, tempo, cliques, primeira escolha, erros, erros recuperados e declaração de função inexistente | M4, M5, M6, M7, M8, MA1 |
| `dados/brutos/testes-usuarios/compreensao.csv` | Resposta de cada participante às perguntas de compreensão e registro de abertura da legenda ou da ajuda | M11 |
| `dados/brutos/testes-usuarios/sus.csv` | Respostas dos dez itens do SUS por participante | M12 |
| `dados/brutos/inspecao/funcoes.csv` | Lista de referência de funções, tarefa associada e verificação de cada avaliador, com evidência | M1 |
| `dados/brutos/inspecao/correcao.csv` | Verificações de dados (coincide ou diverge), indicação de item crítico e evidência | M2 |
| `dados/brutos/inspecao/cenarios-erro.csv` | Resultado de cada cenário C1 a C6 por avaliador, com evidência | M20 |
| `dados/brutos/inspecao/acessibilidade-manual.csv` | Verificações manuais de acessibilidade por página e avaliador | M10 |
| `dados/brutos/acessibilidade/wave/` | Relatórios da extensão WAVE por página | M9 |
| `dados/brutos/flexibilidade/navegadores.csv` | Resultado de cada combinação tarefa × navegador, com captura de tela | M13 |
| `dados/brutos/flexibilidade/paginas-adaptadas.csv` | Resultado de cada verificação página × largura, com os critérios não atendidos | M14 |
| `dados/brutos/flexibilidade/tempos-celular.csv` | Tempos de cada tarefa no computador e no celular, por avaliador | M15 |
| `dados/brutos/desempenho/medicoes.csv` e `dados/brutos/desempenho/lighthouse/` | Uma linha por página, modo do Lighthouse e execução, com data, horário, rede, versões, LCP, total transferido e requisições; relatórios exportados do Lighthouse | M16, M17, M18, M19 |
| `dados/consolidados/metricas.csv` | Valor e nível de cada métrica, no geral, por tarefa e por perfil | Todas |

O formato detalhado de cada arquivo, os instrumentos e o roteiro de execução serão especificados na Fase 3. As gravações não serão publicadas abertamente, por conterem dados pessoais; o acesso a elas será definido na Fase 3, conforme as premissas 5 e 6 do roteiro.

## Referências

[1] ISO/IEC 25023:2016. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality*.

[2] BROOKE, J. SUS: a "quick and dirty" usability scale. In: *Usability Evaluation in Industry*. Taylor & Francis, 1996.

[3] SAURO, J.; LEWIS, J. R. *Quantifying the User Experience: Practical Statistics for User Research*. 2. ed. Morgan Kaufmann, 2016.

[4] W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>. Acesso em: 18 out. 2026.

[5] GOOGLE. *Web Vitals*. web.dev. Disponível em: <https://web.dev/articles/vitals>. Acesso em: 18 out. 2026.

[6] ISO/IEC 25022:2016. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of quality in use*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 17/10/2026 | Definição das métricas M1 a M11 | Felipe Campêlo |
| 1.2 | 18/10/2026 | Numeração e legendas de tabelas; fontes e amostra de M2; instrumento da lista de M1 | Felipe Campêlo |
| 2.0 | 18/10/2026 | Alinhamento à Fase 1 reestruturada: métricas M1 a M19, tarefas T1 a T6, WCAG 2.2 e métricas de Eficiência de Desempenho | Felipe Campêlo |
| 2.1 | 18/10/2026 | Integração da versão complementar: métrica M20 (cenários de erro) e métrica auxiliar MA1; definições comuns; artefatos de dados previstos; critérios de toque e rolagem em M14; recorte de calouros em M5; passo desnecessário em M7; itens críticos e conferências de T1 e T2 em M2; funções por tarefa em M1; P75 complementar em M17; referência à ISO/IEC 25022 | Leonardo Bonetti |
