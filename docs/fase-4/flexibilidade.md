# Flexibilidade (Portabilidade): execução e resultados

<!-- Critérios F4-C1 a F4-C3: execução conforme o plano da Fase 3, dados brutos rastreáveis e cálculo das métricas. -->

Esta página registra a execução das métricas do objetivo **G3 - Flexibilidade (Portabilidade)**: M13 (compatibilidade entre navegadores), M14 (páginas adaptadas a telas pequenas e ao toque) e M15 (tempo relativo no celular). M13 e M14 foram medidas por execução instrumentada; M15 foi medida manualmente, por um avaliador cronometrando as tarefas no computador e em um celular real (seção 5). Para cada métrica, a página mostra o que foi medido, com qual instrumento, como o dado bruto virou valor e o que o valor significa para a questão GQM e para a hipótese correspondentes.

## 1. Rastreabilidade

*Tabela 1 - Da característica ao arquivo de dados.*

| Nível | M13 | M14 | M15 |
| ----- | --- | --- | --- |
| Característica (ISO/IEC 25010:2023) [1] | Flexibilidade, subcaracterística **adaptabilidade** | Flexibilidade, subcaracterística **adaptabilidade** | Flexibilidade, subcaracterística **adaptabilidade** |
| Medida de referência (ISO/IEC 25023:2016) [2] | Adaptabilidade ao ambiente de *software* do sistema (PAd-2-G): o navegador é o ambiente de *software* em que o produto roda no cliente | Adaptabilidade ao ambiente de *hardware* (PAd-1-G): tamanho de tela e entrada por toque | Sem medida equivalente na norma: razão de tempo definida pela equipe ([ficha de M15](../fase-2/metricas.md#m15-tempo-relativo-no-celular)) |
| Questão e hipótese ([Fase 2](../fase-2/hipoteses.md)) | Q14; H14: 22 ou 23 de 24 combinações sem falha (Bom) | Q15; H15: até 5 de 12 verificações adaptadas (Insatisfatório) | Q16; H16: M15 > 1,5 e ≤ 2,0 (Regular) |
| Ficha da métrica | [M13](../fase-2/metricas.md#m13-compatibilidade-entre-navegadores) | [M14](../fase-2/metricas.md#m14-proporcao-de-paginas-adaptadas-a-telas-pequenas-e-ao-toque) | [M15](../fase-2/metricas.md#m15-tempo-relativo-no-celular) |
| Dado bruto | `dados/brutos/flexibilidade/navegadores.csv` e `automatizado/navegadores.jsonl` | `dados/brutos/flexibilidade/paginas-adaptadas.csv` e `automatizado/telas.jsonl` | `dados/brutos/flexibilidade/tempos-celular.csv` e `coleta/calcular_m15.py` |
| Evidências | `dados/brutos/flexibilidade/evidencias/navegadores/` | `dados/brutos/flexibilidade/evidencias/telas/` | Gravações de tela `M15_celular` e `M15_computador`, na pasta restrita da equipe (coluna `evidencia` com o trecho de cada tarefa) |
| Valor consolidado | `dados/consolidados/metricas.csv` | `dados/consolidados/metricas.csv` | `dados/consolidados/metricas.csv` |

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
| Data e horário | 15/11/2026 (Arthur): M13 Chrome e Firefox das 22h39 às 22h42; M14 das 23h19 às 23h23. 21/11/2026 (Felipe): M13 WebKit das 14h54 às 14h55 (com referência no Chrome das 14h53 às 14h54) e Microsoft Edge das 15h39 às 15h40 (horário de Brasília) |
| Produto | Portal do Discente do SIGAA/UnB **v4.15.10.116**, lida no rodapé de cada página em todas as execuções (15/11 e 21/11). A Fase 1 registrou a v4.15.10.115: a versão mudou antes da coleta, como prevê o controle de versão de [Recursos e Ambiente](../fase-3/recursos-ambiente.md#1-produto-avaliado). Todas as medidas desta página são da v4.15.10.116 |
| Computadores | Em 15/11 (Arthur): notebook com 8 GB de memória e Linux (núcleo 6.17), em rede doméstica de banda larga. Em 21/11 (Felipe): Mac com macOS (Darwin 25.6.0), em rede doméstica de banda larga |
| Ferramenta | Playwright 1.65.2 (Python), em modo sem interface gráfica (*headless*) |
| Navegadores (M13) | Google Chrome 146 estável (Linux), Firefox 159 (motor Gecko, compilação do Playwright, Linux), Microsoft Edge 158 estável (macOS) e WebKit 27.2 (motor do Safari, compilação do Playwright, macOS). Versões exatas na coluna `versao` de `navegadores.csv` |
| Telas (M14) | Google Chrome no modo de dispositivo: celular de 360 × 800 px e tablet de 768 × 1024 px, com emulação de toque, de aparelho móvel e *user agent* do Chrome para Android |
| Contas | Em 15/11: conta de estudante de graduação de Arthur, atendendo aos [requisitos de massa de dados](../fase-3/recursos-ambiente.md#41-requisitos-de-cada-conta) de T1 a T6. Em 21/11: conta de estudante de graduação de Felipe, com referência própria no Google Chrome 157 para comparação estrutural das páginas |
| Materiais de T5 | Em 15/11 (Chrome e Firefox): turma *Fundamentos de Redes de Computadores*, download do arquivo "Plano de Ensino" (PDF). Em 21/11 (Edge e WebKit): turma *Técnicas de Programação em Plataformas Emergentes*, visualização de notícia publicada na Turma Virtual (nenhuma turma matriculada na conta tinha arquivo anexado; desvio registrado na seção 7) |

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

Em T5, na coleta de Chrome e Firefox a tarefa exigiu o download do PDF do material; na coleta de Edge e WebKit, por ausência de arquivos anexados nas turmas da conta do avaliador, a verificação abriu uma notícia publicada na Turma Virtual (seção 7). Erros de JavaScript na página são registrados, mas só contam como falha se causarem um dos efeitos da Tabela 3, porque a ficha define falha pelo efeito visível para o estudante.

### 3.2 Resultado

*Tabela 4 - Resultado de M13 por combinação tarefa × navegador.*

| Tarefa | Google Chrome 146 | Firefox 159 | Microsoft Edge 158 | WebKit 27.2 (motor do Safari) |
| ------ | :-: | :-: | :-: | :-: |
| T1 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T1-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T1-firefox-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T1-msedge-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T1-webkit-t1.jpg)) |
| T2 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T2-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T2-firefox-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T2-msedge-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T2-webkit-t1.jpg)) |
| T3 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T3-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T3-firefox-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T3-msedge-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T3-webkit-t1.jpg)) |
| T4 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T4-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T4-firefox-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T4-msedge-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T4-webkit-t1.jpg)) |
| T5 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T5-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T5-firefox-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T5-msedge-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T5-webkit-t1.jpg)) |
| T6 | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T6-chromium-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T6-firefox-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T6-msedge-t1.jpg)) | Sem falha ([captura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/flexibilidade/evidencias/navegadores/T6-webkit-t1.jpg)) |

*Fonte: `dados/brutos/flexibilidade/navegadores.csv`.*

**Valor:** A = 24 combinações sem falha, de B = 24 executadas. **M13 = 24/24 = 100%**, nível **Excelente** (faixa = 100% na Tabela 2 de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#faixas-por-metrica)).

**O que o valor revela:** no computador, o SIGAA funciona igualmente nos três motores de renderização testados (Blink no Chrome e no Edge, Gecko no Firefox e WebKit no Safari): todas as 24 combinações chegaram à página final com os marcadores esperados, sem erros de JavaScript e com o mesmo número de tabelas da execução de referência no Chrome da respectiva conta. A hipótese H14 previa compatibilidade alta com 1 ou 2 falhas pontuais (faixa Bom, 22 ou 23 de 24); o resultado superou a previsão, confirmando que os problemas de Flexibilidade não estão no navegador de computador, e sim em telas pequenas e no toque. A única falha de rede registrada nas 24 execuções é a imagem externa `close12_1.gif`, bloqueada pelo navegador porque o endereço antigo do Yahoo não devolve mais uma imagem; ela não afeta nenhuma tarefa.

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

## 5. Julgamento de Q14 a Q16 e classificação de H14 a H16

M15 foi medida em 22/11/2026 por um avaliador, que executou T1 a T6 pelo caminho mais curto, primeiro no computador e depois no celular (Samsung Galaxy S25 Ultra), com o Google Chrome nos dois aparelhos e na mesma rede Wi-Fi. As duas execuções foram gravadas, e o tempo de cada tarefa vai da fala "começando" à fala "pronto" do avaliador.

*Tabela 8 - Julgamento do objetivo G3.*

| Questão | Métrica | Valor | Nível da questão | Hipótese | Classificação |
| ------- | ------- | ----- | ---------------- | -------- | ------------- |
| Q14 | M13 | 24 de 24 (100%) | **Excelente (3)** | H14: 22 ou 23 de 24 (Bom) | **Refutada** (superou a faixa prevista: Excelente) |
| Q15 | M14 | 0 de 12 (0%) | **Insatisfatório (0)** | H15: até 5 de 12 (Insatisfatório) | **Confirmada** |
| Q16 | M15 | 1,59 (110,2 s no celular para 69,1 s no computador) | **Regular (1)** | H16: 1,5 a 2,0 (Regular) | **Confirmada** |

*Fonte: elaboração da equipe, pelas regras de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#criterios-de-julgamento).*

**Resposta a Q14** (Tabela 4 de Níveis de Pontuação, nível Excelente): **Sim, plenamente.** Todas as seis tarefas foram executadas sem falha nos quatro navegadores de computador (Chrome, Firefox, Edge e WebKit/Safari). H14 é classificada formalmente como **refutada** porque o critério de confirmação exigia a faixa Bom (22 ou 23 de 24), prevendo uma ou duas falhas pontuais que não ocorreram; o resultado é melhor do que o esperado.

**Resposta a Q15** (Tabela 4 de Níveis de Pontuação, nível Insatisfatório): **Não.** As páginas do escopo não se adaptam a telas de celular e tablet: o conteúdo é exibido reduzido, com texto e alvos de toque abaixo dos mínimos, embora os menus respondam ao toque.

**Resposta a Q16** (Tabela 4 de Níveis de Pontuação, nível Regular): **Parcialmente, com dificuldade relevante.** As seis tarefas foram concluídas no celular, mas com 1,59 vez o tempo do computador. A diferença se concentra nas tarefas que exigem ler tabelas pequenas ou tocar em vários alvos: T2 (2,03), T5 (1,96) e T6 (1,89). T3 (1,05) e T4 (1,09), que terminam em um PDF ou na leitura do painel inicial, tiveram tempos parecidos nos dois aparelhos.

**Julgamento de G3:** com Q14 = Excelente (3), Q15 = Insatisfatório (0) e Q16 = Regular (1), a média é 1,33. A questão Insatisfatória (Q15) impede os julgamentos *Atende* e *Atende plenamente*, e o julgamento de Flexibilidade é **Atende parcialmente**. O julgamento das três características está em [Julgamento da Avaliação](julgamento.md).

## 6. Triangulação com o teste com usuários

As duas sessões já realizadas (P1 e P3, do grupo do começo do curso) foram feitas em computador, como prevê o protocolo, mas o questionário aplicado ao fim de cada uma pergunta sobre o uso do SIGAA no celular (item B5). As respostas convergem com as medidas:

*Tabela 9 - Problemas relatados no celular (item B5 do questionário) e critério de M14 correspondente.*

| Problema relatado | P1 | P3 | Critério de M14 | Resultado medido |
| ----------------- | :-: | :-: | --------------- | ---------------- |
| Precisa de zoom e rolagem | Sim | Sim | (a) e (b) | Não atendidos nas 12 verificações |
| Botões pequenos | Sim | Sim | (e) | Não atendido nas 12 verificações |
| Conteúdo cortado | - | Sim | (c) | Não atendido na Turma Virtual (T5) |
| Menu que não abriu | - | Sim | (d) | Atendido na emulação e no celular real de M15, em que o menu Ensino abriu ao toque em T1, T3 e T6 |
| Não conseguiu concluir uma tarefa | Sim | - | (M15) | O avaliador concluiu as seis tarefas no celular, com 1,59 vez o tempo do computador |

*Fonte: `dados/brutos/questionario/respostas.csv` e Tabela 6.*

P3 acessa o SIGAA principalmente pelo celular, o perfil que a Fase 1 associou ao maior impacto de Flexibilidade, e é também o único dos dois que usa ferramenta externa (uma planilha) para planejar o curso. Com dois participantes, a comparação é descritiva; ela mostra, porém, que os problemas medidos são os mesmos que os estudantes percebem, o que reforça a validade de M14 como medida do problema real. Esses dados também alimentam a hipótese de relação HR1 (Flexibilidade → Capacidade de Interação), verificada com M15 em [Julgamento da Avaliação](julgamento.md).

## 7. Desvios em relação ao plano da Fase 3 e ameaças à validade

*Tabela 10 - Desvios do plano e efeito sobre os resultados.*

| Plano da Fase 3 | O que foi feito | Efeito e tratamento |
| --------------- | --------------- | ------------------- |
| M14 em 360 px num **celular real** | Emulação do Chrome com dimensões, toque, escala e *user agent* de um celular Android | O motor de renderização é o mesmo do Chrome para Android. Os critérios que falharam dependem da largura e da falta de *viewport*, que a emulação reproduz. Em M15, executada em um celular real, as páginas também apareceram reduzidas, sem adaptação à tela, e os menus abriram ao toque, o que é coerente com o resultado da emulação |
| M13 em Safari (macOS) | WebKit 27.2 (compilação do Playwright no macOS, mesmo motor de renderização do Safari) | O Playwright automatiza o motor WebKit, não o aplicativo Safari diretamente, de forma análoga ao uso do Firefox compilado pelo Playwright para o motor Gecko. A renderização das páginas e o comportamento dos scripts seguem o motor WebKit nativo do macOS |
| M13 em T5 com download de arquivo | Em Edge e WebKit (21/11), visualização de notícia na Turma Virtual de *Técnicas de Programação em Plataformas Emergentes* (`--modo-t5 noticia`) | Nenhuma turma matriculada na conta de Felipe em 2026.2 tinha arquivo anexado para download. A navegação dentro da Turma Virtual (entrada na turma, menu lateral e abertura de conteúdo publicado) foi exercitada integralmente e comparada contra a execução de referência no Chrome da mesma conta |
| Firefox na versão estável vigente | Firefox 159 da compilação do Playwright (motor Gecko com ajustes para automação), à frente do Firefox estável 155 instalado no sistema | O motor é o mesmo, e os ajustes do Playwright servem para controlar o navegador, sem mudar a renderização |
| Execução por um avaliador em uma conta | Dois avaliadores em contas diferentes (Arthur em Chrome e Firefox; Felipe em Edge e WebKit) | Para que diferenças de histórico entre contas não gerassem falsos positivos na contagem de tabelas, o script executou o Google Chrome também na conta de Felipe como linha de base estrutural (`--apenas-referencia`), mantendo 24 combinações únicas em `navegadores.csv` |
| M15 com média entre avaliadores e navegador padrão do celular | Um avaliador, uma execução por tarefa, com o Google Chrome no celular e no computador | O mesmo navegador nos dois aparelhos isola o efeito do aparelho. Com um avaliador, o valor não tem média; a marcação pela fala tem incerteza de cerca de 0,3 s por tarefa, e o valor só mudaria de nível com um erro de cerca de 6% no tempo total |

*Fonte: elaboração da equipe.*

Outras ameaças: as execuções de M13 foram feitas em duas datas (15/11 e 21/11), ambas na versão **v4.15.10.116** do SIGAA (conferida no rodapé). Como as falhas de M14 vêm de uma causa estrutural, presente em todas as páginas e nas duas larguras, é pouco provável que outra conta ou outro dia mudem o resultado.

## 8. Como reproduzir

Os comandos estão em [`coleta/README.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/coleta/README.md). Em resumo: instalar o Playwright, definir as variáveis `SIGAA_USUARIO` e `SIGAA_SENHA` e rodar `python coleta/sigaa_coleta.py navegadores`, `python coleta/sigaa_coleta.py telas`, `python coleta/borrar.py <evidencias>` e `python coleta/calcular.py`. O cálculo é determinístico: sobre os mesmos registros, produz os mesmos arquivos.

## Referências

[1] ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

[2] ISO/IEC 25023:2016. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement of system and software product quality*.

[3] MICROSOFT. *Playwright*. Documentação oficial. Disponível em: <https://playwright.dev/>. Acesso em: 15 nov. 2026.

[4] W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 15/11/2026 | Execução instrumentada de M13 e M14: método, operacionalização dos critérios, resultados, julgamento de Q14 e Q15, triangulação com o teste com usuários e desvios do plano | [arthurlleite](https://github.com/arthurlleite) |
| 1.1 | 21/11/2026 | Conclusão de M13 com Microsoft Edge 158 e WebKit 27.2 (24/24, Excelente), julgamento de Q14, classificação de H14 e registro dos desvios da coleta no macOS | [Felipe Campêlo](https://github.com/felipeacampelo) |
| 1.2 | 22/11/2026 | Resultado de M15 (1,59, Regular): rastreabilidade, resposta a Q16, H16 confirmada, julgamento de G3 (1,33), triangulação e desvios | Leonardo Bonetti |
