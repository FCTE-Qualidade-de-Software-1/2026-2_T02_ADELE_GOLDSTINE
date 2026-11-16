# Flexibilidade (Portabilidade): execução e resultados

<!-- Critérios F4-C1 a F4-C3: execução conforme o plano da Fase 3, dados brutos rastreáveis e cálculo das métricas. -->

Esta página registra a execução das métricas do objetivo **G3 - Flexibilidade (Portabilidade)**: M13 (compatibilidade entre navegadores) e M14 (páginas adaptadas a telas pequenas e ao toque). M15 (tempo relativo no celular) depende de um avaliador cronometrando as tarefas em um celular real e ainda não foi executada (seção 7). Para cada métrica, a página mostra o que foi medido, com qual instrumento, como o dado bruto virou valor e o que o valor significa para a questão GQM e para a hipótese correspondentes.

## 1. Rastreabilidade

*Tabela 1 - Da característica ao arquivo de dados.*

| Nível | M13 | M14 |
| ----- | --- | --- |
| Característica (ISO/IEC 25010:2023) [1] | Flexibilidade, subcaracterística **adaptabilidade** | Flexibilidade, subcaracterística **adaptabilidade** |
| Medida de referência (ISO/IEC 25023:2016) [2] | Adaptabilidade ao ambiente de *software* do sistema (PAd-2-G): o navegador é o ambiente de *software* em que o produto roda no cliente | Adaptabilidade ao ambiente de *hardware* (PAd-1-G): tamanho de tela e entrada por toque |
| Questão e hipótese ([Fase 2](../fase-2/hipoteses.md)) | Q14; H14: 22 ou 23 de 24 combinações sem falha (Bom) | Q15; H15: até 5 de 12 verificações adaptadas (Insatisfatório) |
| Ficha da métrica | [M13](../fase-2/metricas.md#m13-compatibilidade-entre-navegadores) | [M14](../fase-2/metricas.md#m14-proporcao-de-paginas-adaptadas-a-telas-pequenas-e-ao-toque) |
| Dado bruto | `dados/brutos/flexibilidade/navegadores.csv` e `automatizado/navegadores.jsonl` | `dados/brutos/flexibilidade/paginas-adaptadas.csv` e `automatizado/telas.jsonl` |
| Evidências | `dados/brutos/flexibilidade/evidencias/navegadores/` | `dados/brutos/flexibilidade/evidencias/telas/` |
| Valor consolidado | `dados/consolidados/metricas.csv` | `dados/consolidados/metricas.csv` |

*Fonte: elaboração da equipe.*

A ISO/IEC 25023:2016 ainda usa o nome Portabilidade, que a ISO/IEC 25010:2023 trocou por Flexibilidade. As duas medidas da norma têm a forma X = A/B, a mesma das fichas de M13 e M14.

## 2. Método: execução instrumentada

O plano da Fase 3 previa executar M13 e M14 manualmente: um avaliador abre cada página em cada navegador e largura de tela e anota se cada critério foi atendido ([Recursos e Ambiente](../fase-3/recursos-ambiente.md#2-hardware-e-software-por-metodo)). Para M14, isso exige julgamentos difíceis de repetir com exatidão, como "a fonte está abaixo de 12 px?" ou "o botão tem 24 × 24 px?", medidos à mão no inspetor de elementos, página por página.

A equipe **instrumentou** essa execução: um *script* versionado ([`coleta/sigaa_coleta.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/tree/main/coleta)) usa o Playwright [3], biblioteca que controla navegadores reais por programa, para entrar no SIGAA, executar T1 a T6 pelo caminho principal da [Fase 1](../fase-1/escopo.md#21-tarefas-representativas) e, na página final de cada tarefa, medir os critérios com as próprias APIs do navegador. As vantagens para o rigor da avaliação são:

- **Repetibilidade e reprodutibilidade:** o mesmo *script*, rodado de novo por qualquer membro, aplica exatamente o mesmo procedimento; a ficha de cada critério está no código, não na memória do avaliador.
- **Objetividade:** os critérios viram medidas (larguras em px, tamanhos de fonte, áreas de toque), registradas por página em `telas.jsonl`, e não um "sim" ou "não" de quem olhou a tela.
- **Exaustividade:** em vez de amostrar alguns textos e botões, o *script* mede **todos** os textos visíveis e **todos** os controles de cada página.

O que a automação **não** substitui foi mantido manual: a conferência visual das capturas, que decidiu os casos limítrofes do critério (c) (seção 4.3), e M15, que mede o esforço de uma pessoa.

### 2.1 Ambiente

*Tabela 2 - Ambiente da execução instrumentada.*

| Item | Especificação |
| ---- | ------------- |
| Data e horário | 15/11/2026: M13 das 22h39 às 22h42; M14 das 23h19 às 23h23 (horário de Brasília) |
| Produto | Portal do Discente do SIGAA/UnB **v4.15.10.116**, lida no rodapé de cada página. A Fase 1 registrou a v4.15.10.115: a versão mudou antes da coleta, como prevê o controle de versão de [Recursos e Ambiente](../fase-3/recursos-ambiente.md#1-produto-avaliado). Todas as medidas desta página são da v4.15.10.116 |
| Computador | Notebook com 8 GB de memória e Linux (núcleo 6.17), em rede doméstica de banda larga |
| Ferramenta | Playwright 1.65 (Python), em modo sem interface gráfica (*headless*) |
| Navegadores (M13) | Google Chrome 146 estável, instalado no sistema; Firefox 159 (motor Gecko, compilação do Playwright). Versões exatas na coluna `versao` de `navegadores.csv` |
| Telas (M14) | Google Chrome no modo de dispositivo: celular de 360 × 800 px e tablet de 768 × 1024 px, com emulação de toque, de aparelho móvel e *user agent* do Chrome para Android |
| Conta | Conta de estudante de graduação de um membro da equipe, que atende aos [requisitos de massa de dados](../fase-3/recursos-ambiente.md#41-requisitos-de-cada-conta) de T1 a T6 |
| Materiais de T5 | Turma *Fundamentos de Redes de Computadores*, arquivo "Plano de Ensino" (PDF publicado pelo professor) |

*Fonte: elaboração da equipe; valores registrados em cada linha dos arquivos `.jsonl`.*

### 2.2 Regras éticas e de proteção de dados

A coleta segue as premissas da Fase 1 de não alterar dados nem sobrecarregar o ambiente de produção ([Escopo](../fase-1/escopo.md#6-premissas-e-restricoes)):

- **Só consultas.** O *script* só aciona os itens de menu de uma lista fechada (Consultar Minhas Notas, Emitir Atestado de Matrícula, Consultar Índices Acadêmicos e Calendário Acadêmico). Itens como Trancar ou Realizar Matrícula nunca são clicados.
- **Carga mínima.** Uma sessão por vez, com 3 s de pausa entre as tarefas. O volume equivale ao de um estudante navegando.
- **Credenciais.** Lidas só de variáveis de ambiente; não aparecem em nenhum arquivo do repositório.
- **Dados pessoais.** Os registros `.jsonl` não guardam o texto das páginas, só medidas e uma assinatura estrutural (número de tabelas, linhas e *links*). As capturas publicadas recebem **dois borrões**: o texto e as imagens são desfocados por CSS no momento da captura e, depois, toda a imagem recebe um desfoque gaussiano (`coleta/borrar.py`). Nome, matrícula, notas e foto ficam ilegíveis, e a estrutura que a evidência precisa mostrar (tabelas, menus, larguras e sobreposições) continua visível. As capturas originais ficaram fora do repositório, com o avaliador.

### 2.3 Falhas intermitentes do servidor

Durante os testes do *script*, o SIGAA devolveu duas vezes páginas **sem CSS nem JavaScript**: o menu não era montado, e diálogos que deveriam estar ocultos apareciam na tela. A falha some ao recarregar e não depende do navegador. Para que ela não fosse contada como incompatibilidade de navegador (M13) nem como página não adaptada (M14), o *script* verifica, em cada página, se o menu foi montado e se todas as folhas de estilo carregaram e, se não, repete a tarefa (até três vezes), registrando cada tentativa. Nas execuções registradas, nenhuma tarefa precisou ser repetida, e a única requisição que falhou foi a de uma imagem externa que o SIGAA referencia em todas as páginas e que não existe mais (`close12_1.gif`, em um servidor antigo do Yahoo).

## 3. M13 - Compatibilidade entre navegadores

### 3.1 Procedimento

Para cada combinação tarefa × navegador, o *script* executa a tarefa em uma janela de 1366 × 768 px e a classifica como **com falha** se ocorrer qualquer evento da ficha de M13, operacionalizado assim:

*Tabela 3 - Critérios de falha da ficha de M13 e como foram verificados.*

| Falha (ficha de M13) | Verificação |
| -------------------- | ----------- |
| Elemento que não carrega | Erro de execução ao procurar um elemento do caminho, ou recurso do SIGAA com erro de carregamento |
| Botão que não responde | O clique não leva à página seguinte do caminho (tempo-limite de navegação) |
| Layout quebrado que impede a leitura | A página final não contém os textos que comprovam a conclusão da tarefa (ex.: "Turmas Matriculadas" em T3, "Trancamento de Turmas" em T6) |
| Resultado diferente do obtido no Chrome | Número de tabelas da página final diferente do obtido no Chrome na mesma tarefa |

*Fonte: elaboração da equipe, a partir da ficha de M13.*

Em T5, a tarefa só conta como concluída se o PDF do material for de fato baixado. Erros de JavaScript na página são registrados, mas só contam como falha se causarem um dos efeitos da Tabela 3, porque a ficha define falha pelo efeito visível para o estudante.

### 3.2 Resultado

*Tabela 4 - Resultado de M13 por combinação tarefa × navegador.*

| Tarefa | Google Chrome 146 | Firefox 159 | Microsoft Edge | Safari |
| ------ | :-: | :-: | :-: | :-: |
| T1 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T1-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T1-firefox-t1.jpg)) | Pendente | Pendente |
| T2 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T2-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T2-firefox-t1.jpg)) | Pendente | Pendente |
| T3 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T3-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T3-firefox-t1.jpg)) | Pendente | Pendente |
| T4 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T4-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T4-firefox-t1.jpg)) | Pendente | Pendente |
| T5 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T5-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T5-firefox-t1.jpg)) | Pendente | Pendente |
| T6 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T6-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T6-firefox-t1.jpg)) | Pendente | Pendente |

*Fonte: `dados/brutos/flexibilidade/navegadores.csv`.*

**Valor:** A = 12 combinações sem falha, de B = 12 executadas. Faltam as 12 combinações de Edge e Safari, então o valor final de M13 = A/24 ficará entre 12/24 (50%, se todas falharem) e 24/24 (100%). Pela regra 1 de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#regra-1-metricas-nao-aplicaveis), **M13 ainda não recebe nível**.

**O que o valor revela:** no computador, o SIGAA funciona igualmente nos dois motores de renderização testados (Blink e Gecko): todas as tarefas chegaram à página final com o mesmo conteúdo, e o PDF de T5 foi baixado nos dois. A hipótese H14 previa justamente que os problemas de Flexibilidade não estariam no navegador de computador, mas em telas pequenas e no toque, e o resultado parcial vai nessa direção. A única falha de rede registrada nas 12 execuções é a imagem externa `close12_1.gif`, bloqueada pelo navegador (`ERR_BLOCKED_BY_ORB`) porque o endereço antigo do Yahoo não devolve mais uma imagem; ela não afeta nenhuma tarefa.

## 4. M14 - Páginas adaptadas a telas pequenas e ao toque

### 4.1 Operacionalização dos critérios

A ficha de M14 considera uma página adaptada se ela atender aos cinco critérios (a) a (e). A Tabela 5 mostra como cada um foi medido.

*Tabela 5 - Critérios de M14 e medida usada.*

| Critério da ficha | Medida automática | Atende se |
| ----------------- | ----------------- | --------- |
| (a) Sem rolagem horizontal da página, sem zoom (critério 1.4.10 da WCAG 2.2 [4]) | Largura do *layout* (`documentElement.clientWidth`), largura do conteúdo (`scrollWidth`) e escala de exibição (`visualViewport.scale`) | A página é montada na largura do aparelho e o conteúdo cabe nela |
| (b) Nenhum texto da tarefa com fonte menor que 12 px | Tamanho de fonte calculado (`getComputedStyle`) de **cada** texto visível, multiplicado pela escala de exibição (tamanho efetivo na tela) | Nenhum texto com tamanho efetivo < 12 px |
| (c) Nenhum elemento sobreposto ou cortado | Caixas reais de cada trecho de texto (`Range.getClientRects`), comparadas entre si e com botões e imagens; elementos com conteúdo maior que a área visível e corte (`overflow: hidden`) | Nenhum texto coberto em mais de 25% da sua área e nenhum texto cortado, após conferência visual |
| (d) Menus usados na tarefa acionáveis por toque | Toque (evento de toque, não de ponteiro) no menu Ensino e no menu lateral Materiais da Turma Virtual; verificação de que o submenu ficou visível | Todos os submenus da tarefa abrem ao toque |
| (e) Área de toque de pelo menos 24 × 24 px (critério 2.5.8 da WCAG 2.2) | Tamanho efetivo de **todos** os controles visíveis da página final e dos controles tocados no caminho, com as exceções do critério 2.5.8: *link* dentro de frase e espaçamento equivalente (um círculo de 24 px centrado no alvo não toca outro alvo) | Nenhum controle abaixo de 24 px sem exceção aplicável |

*Fonte: elaboração da equipe, a partir da ficha de M14 e da WCAG 2.2.*

**Por que a escala de exibição importa.** Quando a página não declara a *viewport* (`<meta name="viewport">`), o navegador do celular a monta como se a tela tivesse 980 px e depois a reduz para caber na largura real. A página "cabe" na tela, mas tudo fica menor: em 360 px, a escala é de 360/980 ≈ 0,37, e um texto de 11 px passa a ter cerca de 4 px na tela. Por isso, (a) não é atendido só porque não aparece barra de rolagem: a ficha pede a página **sem zoom**, e, para ler o texto, o estudante precisa ampliar a página e, então, rolar na horizontal, como relatado na observação OP-03 da [Fase 1](../fase-1/software-avaliado.md#4-observacoes-preliminares-da-interface). Pelo mesmo motivo, (b) e (e) usam o tamanho **efetivo**, isto é, o tamanho em CSS multiplicado pela escala.

**Por que (c) teve conferência visual.** O detector de sobreposição apontou casos que não são defeito de *layout*: o aviso de cookies, uma camada fixa que cobre parte da tela até o estudante tocar em "Ciente", e botões de diálogos ocultos posicionados fora da tela. Esses casos foram excluídos da medida, e a regra de exclusão está no código. Os casos restantes foram conferidos nas capturas.

### 4.2 Páginas verificadas

As páginas são as páginas finais de T1 a T6 ([Recursos e Ambiente, seção 4.1](../fase-3/recursos-ambiente.md#41-requisitos-de-cada-conta)). Em T4, o caminho principal da Fase 1 leva à página **Índices Acadêmicos**. O protocolo do teste com usuários restringiu T4 à carga horária cumprida e pendente, que também aparece no painel **Integralizações** da página inicial; essa página já é verificada em T2, então os resultados de T2 valem também para o painel.

### 4.3 Resultado

*Tabela 6 - Medidas de M14 por página e largura.*

| Tarefa | Largura (px) | Escala | Largura do *layout* (px) | Menor fonte efetiva (px) | Textos < 12 px | Textos sobrepostos ou cobertos | Menu ao toque | Controles < 24 px sem exceção | (a) | (b) | (c) | (d) | (e) | Adaptada | Evidência |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| T1 | 360 | 0,37 | 980 | 3,3 | 427 de 427 | 0 | Abriu | 1 de 7 na página; 2 de 2 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T1-celular_360.jpg) |
| T2 | 360 | 0,37 | 980 | 3,3 | 148 de 148 | 0 | Sem menu | 29 de 52 na página; 0 de 0 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T2-celular_360.jpg) |
| T3 | 360 | 0,37 | 980 | 3,3 | 215 de 215 | 0 | Abriu | 2 de 7 na página; 2 de 2 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T3-celular_360.jpg) |
| T4 | 360 | 0,37 | 980 | 3,8 | 49 de 49 | 0 | Abriu | 2 de 7 na página; 2 de 2 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T4-celular_360.jpg) |
| T5 | 360 | 0,37 | 980 | 2,9 | 112 de 112 | 3 | Abriu | 18 de 38 na página; 3 de 3 no caminho | nao | nao | nao | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T5-celular_360.jpg) |
| T6 | 360 | 0,37 | 980 | 3,4 | 112 de 112 | 0 | Abriu | 12 de 18 na página; 3 de 3 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T6-celular_360.jpg) |
| T1 | 768 | 0,78 | 980 | 7,1 | 427 de 427 | 0 | Abriu | 0 de 7 na página; 2 de 2 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T1-tablet_768.jpg) |
| T2 | 768 | 0,78 | 980 | 7,0 | 148 de 148 | 0 | Sem menu | 10 de 52 na página; 0 de 0 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T2-tablet_768.jpg) |
| T3 | 768 | 0,78 | 980 | 7,0 | 215 de 215 | 0 | Abriu | 0 de 7 na página; 2 de 2 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T3-tablet_768.jpg) |
| T4 | 768 | 0,78 | 980 | 8,2 | 49 de 49 | 0 | Abriu | 0 de 7 na página; 2 de 2 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T4-tablet_768.jpg) |
| T5 | 768 | 0,78 | 980 | 6,3 | 112 de 112 | 4 | Abriu | 8 de 38 na página; 3 de 3 no caminho | nao | nao | nao | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T5-tablet_768.jpg) |
| T6 | 768 | 0,78 | 980 | 7,3 | 112 de 112 | 0 | Abriu | 6 de 18 na página; 3 de 3 no caminho | nao | nao | sim | sim | nao | **nao** | [captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/telas/T6-tablet_768.jpg) |

*Fonte: `dados/brutos/flexibilidade/paginas-adaptadas.csv` e `automatizado/telas.jsonl`. Escala = `visualViewport.scale`; fonte efetiva = tamanho CSS × escala; nos controles, "no caminho" são os itens tocados para chegar à página (menu Ensino, item do submenu, nome da turma, lupa do calendário, menu Materiais e material).*

**Valor:** A = 0 páginas adaptadas, de B = 12 verificações. **M14 = 0/12 = 0%**, nível **Insatisfatório** (faixa < 50%, ou seja, 5 ou menos das 12).

*Tabela 7 - Critérios não atendidos, por largura (6 páginas em cada).*

| Critério | 360 px | 768 px | Causa |
| -------- | :----: | :----: | ----- |
| (a) Sem rolagem horizontal, sem zoom | 6 de 6 não atendem | 6 de 6 não atendem | Nenhuma página declara a *viewport*; o *layout* tem 980 px e é reduzido para caber na tela |
| (b) Fonte de pelo menos 12 px | 6 de 6 não atendem | 6 de 6 não atendem | Efeito da redução: **nenhum** dos 1.063 textos visíveis das seis páginas atinge 12 px efetivos |
| (c) Nada sobreposto ou cortado | 1 de 6 não atende (T5) | 1 de 6 não atende (T5) | Na Turma Virtual, os botões da barra superior cobrem o título e o período da turma |
| (d) Menus acionáveis por toque | Atendido nas 6 | Atendido nas 6 | O menu Ensino e o menu Materiais abriram com evento de toque |
| (e) Alvos de pelo menos 24 × 24 px | 6 de 6 não atendem | 6 de 6 não atendem | Menus e *links* ficam com 4 a 19 px de altura efetiva; o item Ensino tem 22,8 × 8,8 px em 360 px |

*Fonte: Tabela 6.*

**O que os dados revelam.** As 12 falhas têm **uma causa raiz comum**: o SIGAA não tem *layout* responsivo nem declara a *viewport*. O navegador do celular então monta a página com 980 px e a reduz a 37% (360 px) ou 78% (768 px). A página "cabe" na tela, mas tudo fica proporcionalmente menor: em 360 px, a menor fonte de cada página fica entre 2,9 e 3,8 px efetivos, um quarto dos 12 px exigidos, e o item Ensino, por onde passam T1, T3, T4 e T6, vira um alvo de 22,8 × 8,8 px, menos da metade da altura mínima do critério 2.5.8 da WCAG 2.2. Para ler, o estudante precisa ampliar a página com o gesto de pinça e, então, rolar na horizontal, como descrevia a observação OP-03. Mesmo em 768 px (tablet), nenhum texto chega a 12 px. Por isso, o resultado não depende de ajustes pontuais: **enquanto o *layout* for fixo em 980 px, nenhuma página do escopo pode ser adaptada**, e a correção de qualquer página passa pela mesma mudança estrutural.

Dois resultados contrariam parte das expectativas da Fase 1:

- **Os menus abrem ao toque (critério d).** A observação OP-02 previa menus suspensos sem equivalente para o toque. Na emulação, os navegadores convertem o toque nos eventos de ponteiro que o menu espera, e todos os submenus abriram. O problema dos menus no celular é o tamanho do alvo (critério e), não a falta de resposta ao toque. Como o participante P3 relatou um menu que não abriu no celular (seção 6), o ponto será conferido em aparelho real.
- **A Turma Virtual é a única página com conteúdo encoberto (critério c),** e só nas larguras menores: em 1366 px o título da turma aparece inteiro, e em 980 px de *layout* ele é cortado pelos botões Imprimir e Trocar Turma (aparece "…REDES DE COMPUTAD"). É um defeito de adaptação, e não de navegador.

**Modo Mobile.** O rodapé de todas as páginas tem um *link* "Modo Mobile | Modo Clássico". Mesmo recebendo o *user agent* de um celular Android, o SIGAA entregou o modo clássico, e o *link* para a versão móvel fica no fim da página, com o mesmo texto reduzido das demais. A avaliação mede as páginas que o estudante recebe ao acessar o sistema, como define a ficha de M14; a cobertura de T1 a T6 pelo Modo Mobile não foi verificada nesta execução e fica registrada como ponto a examinar.

## 5. Julgamento de Q14 e Q15 e classificação de H14 e H15

*Tabela 8 - Julgamento parcial do objetivo G3.*

| Questão | Métrica | Valor | Nível da questão | Hipótese | Classificação |
| ------- | ------- | ----- | ---------------- | -------- | ------------- |
| Q14 | M13 | 12 de 12 executadas (parcial, 12 de 24 combinações) | Sem nível (regra 1) | H14: 22 ou 23 de 24 (Bom) | Inconclusiva por enquanto |
| Q15 | M14 | 0 de 12 (0%) | **Insatisfatório (0)** | H15: até 5 de 12 (Insatisfatório) | **Confirmada** |
| Q16 | M15 | Não executada | Sem dados | H16: 1,5 a 2,0 (Regular) | Inconclusiva por enquanto |

*Fonte: elaboração da equipe, pelas regras de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#criterios-de-julgamento).*

**Resposta a Q15** (Tabela 4 de Níveis de Pontuação, nível Insatisfatório): **Não.** As páginas do escopo não se adaptam a telas de celular e tablet: o conteúdo é exibido reduzido, com texto e alvos de toque abaixo dos mínimos, embora os menus respondam ao toque.

**G3 ainda não pode ser julgado:** duas das três questões estão sem dados, e a regra de julgamento classifica como *inconclusivo* um objetivo com mais da metade das questões sem dados. O resultado de Q15 já restringe o julgamento final: como uma questão Insatisfatória impede os julgamentos *atende* e *atende plenamente*, Flexibilidade será julgada, no máximo, como **atende parcialmente**, quaisquer que sejam os resultados de M13 e M15.

## 6. Triangulação com o teste com usuários

As duas sessões já realizadas (P1 e P3, do grupo do começo do curso) foram feitas em computador, como prevê o protocolo, mas o questionário aplicado ao fim de cada uma pergunta sobre o uso do SIGAA no celular (item B5). As respostas convergem com as medidas:

*Tabela 9 - Problemas relatados no celular (item B5 do questionário) e critério de M14 correspondente.*

| Problema relatado | P1 | P3 | Critério de M14 | Resultado medido |
| ----------------- | :-: | :-: | --------------- | ---------------- |
| Precisa de zoom e rolagem | Sim | Sim | (a) e (b) | Não atendidos nas 12 verificações |
| Botões pequenos | Sim | Sim | (e) | Não atendido nas 12 verificações |
| Conteúdo cortado | - | Sim | (c) | Não atendido na Turma Virtual (T5) |
| Menu que não abriu | - | Sim | (d) | Atendido na emulação; a conferir em aparelho real |
| Não conseguiu concluir uma tarefa | Sim | - | (M15, não executada) | - |

*Fonte: `dados/brutos/questionario/respostas.csv` e Tabela 6.*

P3 acessa o SIGAA principalmente pelo celular, o perfil que a Fase 1 associou ao maior impacto de Flexibilidade, e é também o único dos dois que usa ferramenta externa (uma planilha) para planejar o curso. Com dois participantes, a comparação é descritiva; ela mostra, porém, que os problemas medidos são os mesmos que os estudantes percebem, o que reforça a validade de M14 como medida do problema real. Esses dados também alimentam a hipótese de relação HR1 (Flexibilidade → Capacidade de Interação), que só pode ser verificada com M15.

## 7. Desvios em relação ao plano da Fase 3 e ameaças à validade

*Tabela 10 - Desvios do plano e efeito sobre os resultados.*

| Plano da Fase 3 | O que foi feito | Efeito e tratamento |
| --------------- | --------------- | ------------------- |
| M14 em 360 px num **celular real** | Emulação do Chrome com dimensões, toque, escala e *user agent* de um celular Android | O motor de renderização é o mesmo do Chrome para Android. Os critérios que falharam dependem da largura e da falta de *viewport*, que a emulação reproduz. A verificação em um celular real fica para M15, que usa o mesmo aparelho, e confirma ou não os resultados |
| M13 em Chrome, Firefox, **Edge e Safari** | Chrome e Firefox (12 das 24 combinações) | O Safari exige macOS, e o motor WebKit do Playwright não roda neste sistema sem bibliotecas que exigem permissão de administrador. O Edge não estava instalado. Pela regra 1 de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#regra-1-metricas-nao-aplicaveis), M13 fica sem nível até as 12 combinações restantes serem executadas manualmente, como previa a tarefa T08 do [cronograma](../fase-3/cronograma.md) |
| Firefox na versão estável vigente | Firefox 159 da compilação do Playwright (motor Gecko com ajustes para automação), à frente do Firefox estável 155 instalado no sistema | O motor é o mesmo, e os ajustes do Playwright servem para controlar o navegador, sem mudar a renderização. Como a versão é mais nova que a estável, o resultado do Firefox é confirmado na execução manual da T08, junto com Edge e Safari |
| Execução por um avaliador | Execução por *script* e conferência visual por um avaliador | Ganho de objetividade nos critérios de M14. O *script* e os dados brutos estão no repositório para que outro membro repita a coleta |
| M15 | Não executada | Depende de um avaliador cronometrando as tarefas em celular real; segue no cronograma (T08) |

*Fonte: elaboração da equipe.*

Outras ameaças: os resultados são de uma única conta e de um único dia, e o SIGAA pode mudar de versão antes do fim da Fase 4 (a versão de cada medida está registrada). Como as falhas de M14 vêm de uma causa estrutural, presente em todas as páginas e nas duas larguras, é pouco provável que outra conta ou outro dia mudem o resultado.

## 8. Como reproduzir

Os comandos estão em [`coleta/README.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/coleta/README.md). Em resumo: instalar o Playwright, definir as variáveis `SIGAA_USUARIO` e `SIGAA_SENHA` e rodar `python coleta/sigaa_coleta.py navegadores`, `python coleta/sigaa_coleta.py telas`, `python coleta/borrar.py dados/brutos/flexibilidade/evidencias` e `python coleta/calcular.py`. O cálculo é determinístico: sobre os mesmos registros, produz os mesmos arquivos.

## Referências

[1] ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

[2] ISO/IEC 25023:2016. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality*.

[3] MICROSOFT. *Playwright*. Documentação oficial. Disponível em: <https://playwright.dev/>. Acesso em: 15 nov. 2026.

[4] W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 15/11/2026 | Execução instrumentada de M13 e M14: método, operacionalização dos critérios, resultados, julgamento de Q14 e Q15, triangulação com o teste com usuários e desvios do plano | [arthurlleite](https://github.com/arthurlleite) |
