# Coleta automatizada (Flexibilidade e desempenho)

Scripts que executam as tarefas T1 a T6 no SIGAA/UnB com o [Playwright](https://playwright.dev/) e produzem os dados brutos de M13 e M14 e os dados complementares de desempenho. O método, as decisões e os resultados estão na GitPage, em **Fase 4 > Flexibilidade** e **Fase 4 > Desempenho (complementar)**.

| Arquivo | Função |
| ------- | ------ |
| `sigaa_coleta.py` | Faz login com a conta do avaliador, executa as tarefas e grava um registro JSON por execução e as capturas de tela |
| `coleta_wave.py` | Injeta o motor oficial da extensão WAVE (`wave.min.js`) nas páginas finais de T1 a T6, grava os relatórios JSON sanitizados e gera `dados/brutos/acessibilidade/wave/resumo.csv` |
| `borrar.py` | Aplica o segundo borrão nas capturas publicáveis (dados pessoais ilegíveis) |
| `calcular.py` | Gera `navegadores.csv`, `paginas-adaptadas.csv`, `dados/consolidados/desempenho.csv` e as linhas de M9, M13 e M14 em `metricas.csv` |
| `calcular_testes.py` | Gera as linhas de M3, M4, M5, M6, M7, M8, M11, M12, MA1, IQ1 a IQ4 e HP1 em `metricas.csv` a partir das planilhas do teste com usuários e do questionário |
| `graficos_testes.py` | Gera os gráficos SVG/PNG de `docs/assets/graficos/teste-usuarios/` e injeta os gráficos com tabelas via hook do MkDocs (`[[GRAFICO_TU:...]]`) |
| `inspecao_coleta.py` | Primeiro avaliador automatizado da inspeção: critérios (a) a (d) de M10 nas páginas de T1 a T6, cenários C1 a C6 de M20, menus do portal (M1) e, com `documentos`, as páginas e o histórico usados em M2, gravados só numa pasta local fora do repositório |
| `calcular_inspecao.py` | Gera as linhas de M1, M2, M10 e M20 em `metricas.csv` a partir das colunas `*_final` de `dados/brutos/inspecao/` |
| `matriz_dispositivos.py` | Matriz multiplataforma (dado complementar): login e T1 a T6 em 20 perfis de computador (Windows, macOS, Linux), celular (Android, iOS) e tablet (iPadOS, Android), com 7 navegadores (Chrome, Chromium, Edge, Brave, Opera, Firefox e Safari/WebKit; o Vivaldi trava sob automação); grava `dados/brutos/flexibilidade/automatizado/matriz.jsonl` e capturas borradas da área visível |
| `calcular_matriz.py` | Aplica os critérios de M14 à largura de cada aparelho e gera `dados/consolidados/matriz-dispositivos.csv` e `matriz-resumo.csv` (não altera `metricas.csv`) |
| `graficos_finais.py` | Gera os gráficos da síntese final (16 métricas, hipóteses, julgamento, matriz, fontes no celular e desempenho) em `docs/assets/graficos/final/` e os injeta nas páginas via hook do MkDocs (`[[GRAFICO_FINAL:...]]`) |
| `prototipo_mobile.py` | Gera as telas SVG/PNG (`docs/assets/prototipo-mobile/`) e o simulador HTML interativo do Protótipo Mobile-First via hook do MkDocs (`[[PROTOTIPO_MOBILE_INTERATIVO]]`) |
| `verificar_prototipo.py` | Verificação da ação de melhoria: aplica ao protótipo mobile os mesmos critérios de M14 (e, com `--wave-js`, o WAVE de M9) e grava `dados/brutos/flexibilidade/automatizado/telas-prototipo.jsonl`, as capturas em `dados/brutos/flexibilidade/evidencias/prototipo/` e `dados/consolidados/verificacao-prototipo.csv`, sem alterar `metricas.csv` |

## Regras de segurança da coleta

- **Só consultas.** O script só aciona os itens de menu de uma lista fechada (`MENU_PERMITIDO`): Consultar Minhas Notas, Emitir Atestado de Matrícula, Consultar Índices Acadêmicos e Calendário Acadêmico. Itens como Trancar, Retirar Matrícula ou Realizar Matrícula nunca são clicados.
- **Carga mínima no servidor.** Uma sessão por vez, com 3 s de pausa entre as tarefas; o volume equivale ao de um estudante navegando.
- **Credenciais fora do código.** Usuário e senha vêm só das variáveis de ambiente `SIGAA_USUARIO` e `SIGAA_SENHA` e não são gravados em nenhum arquivo.
- **Dados pessoais.** Os registros JSON não guardam texto das páginas, apenas medidas (tamanhos, contagens, tempos) e uma assinatura estrutural (número de tabelas e linhas). As capturas publicadas no repositório têm o texto e as imagens borrados duas vezes (CSS no momento da captura e desfoque gaussiano em `borrar.py`). As capturas originais só são gravadas com `--local`, numa pasta que o script recusa se estiver dentro do repositório.

## Como reproduzir

```bash
python -m venv .venv && . .venv/bin/activate
pip install playwright pillow
playwright install chromium firefox webkit   # navegadores do Playwright
# Google Chrome e Microsoft Edge estáveis precisam estar instalados no sistema (canais "chrome" e "msedge").

export SIGAA_USUARIO=...                      # matrícula do avaliador
read -s SIGAA_SENHA && export SIGAA_SENHA     # senha digitada sem eco

python coleta/sigaa_coleta.py navegadores --local ~/sigaa-originais   # M13 (todos os navegadores)
# Para rodar navegadores específicos em outra conta mantendo referência estrutural própria no Chrome:
# python coleta/sigaa_coleta.py navegadores --navegadores chrome --avaliador Felipe --apenas-referencia --turma-t5 "TURMA" --modo-t5 noticia
# python coleta/sigaa_coleta.py navegadores --navegadores webkit edge --avaliador Felipe --turma-t5 "TURMA" --modo-t5 noticia
python coleta/sigaa_coleta.py telas --local ~/sigaa-originais         # M14
python coleta/sigaa_coleta.py desempenho --repeticoes 5               # desempenho
python coleta/coleta_wave.py --wave-js /caminho/para/wave.min.js      # M9 (WAVE oficial)
python coleta/borrar.py dados/brutos/flexibilidade/evidencias         # aceita pasta ou arquivos específicos
python coleta/calcular.py
python coleta/inspecao_coleta.py m10 --turma-t5 "TURMA" --material-t5 "ARQUIVO.pdf"   # M10
python coleta/inspecao_coleta.py m20                   # M20 (C1 real: inspecao_coleta.py c1-real, ~42 min)
python coleta/inspecao_coleta.py documentos --local ~/sigaa-originais/inspecao   # M1 e M2 (fora do repositório)
python coleta/calcular_inspecao.py
```

Os registros são acrescentados aos arquivos `.jsonl`; para refazer uma coleta do zero, apague o `.jsonl` correspondente antes. Os valores dependem do horário, da rede e do nó do servidor que atendeu a sessão (registrado em cada linha, campo `assinatura.rodape`).

## Matriz multiplataforma

Os navegadores fora do Playwright são extraídos dos pacotes oficiais, sem instalação no sistema (sem `sudo`), em `~/.cache/sigaa-navegadores/` (ou nos caminhos das variáveis `SIGAA_EDGE`, `SIGAA_BRAVE`, `SIGAA_OPERA` e `SIGAA_VIVALDI`):

```bash
B=~/.cache/sigaa-navegadores; mkdir -p $B && cd $B
curl -LO https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_<versão>_amd64.deb && dpkg -x microsoft-edge-stable_*.deb edge
curl -LO https://github.com/brave/brave-browser/releases/download/v<versão>/brave-browser-<versão>-linux-amd64.zip && unzip -d brave brave-browser-*.zip
curl -LO https://deb.opera.com/opera-stable/pool/non-free/o/opera-stable/opera-stable_<versão>_amd64.deb && dpkg -x opera-stable_*.deb opera
curl -LO https://repo.vivaldi.com/archive/deb/pool/main/vivaldi-stable_<versão>_amd64.deb && dpkg -x vivaldi-stable_*.deb vivaldi
cd -
python coleta/matriz_dispositivos.py --listar     # perfis disponíveis
python coleta/matriz_dispositivos.py              # todos (cerca de 1 min por perfil)
python coleta/calcular_matriz.py
python coleta/graficos_finais.py
```

Em distribuições que o Playwright não suporta oficialmente, o WebKit pode precisar de bibliotecas do Ubuntu 24.04 (`libicu74`, `libevent-2.1-7t64`, `libavif16`, `libmanette-0.2-0`, `libhidapi-hidraw0`); basta extrair os `.deb` com `dpkg -x` e ligar os `.so` em `~/.cache/ms-playwright/webkit-*/minibrowser-wpe/sys/lib/`. O que a emulação reproduz e o que não reproduz está na GitPage, em **Fase 4 > Matriz Multiplataforma**.

## Saídas

| Arquivo | Conteúdo |
| ------- | -------- |
| `dados/brutos/flexibilidade/automatizado/navegadores.jsonl` | Uma linha por tarefa e navegador (e por tentativa) |
| `dados/brutos/flexibilidade/automatizado/telas.jsonl` | Uma linha por tarefa e largura (360 e 768 px), com as medidas dos critérios de M14 |
| `dados/brutos/desempenho/automatizado/execucoes.jsonl` | Uma linha por tarefa, cenário e repetição, com as medidas de Navigation Timing e Paint Timing de cada página |
| `dados/brutos/acessibilidade/wave/` | Relatórios JSON sanitizados (`T1-wave.json` a `T6-wave.json`) e resumo tabular (`resumo.csv`) de M9 |
| `dados/brutos/flexibilidade/automatizado/matriz.jsonl` | Uma linha por perfil e página (login e T1 a T6), com conclusão, medidas de adaptação e tempos |
| `dados/brutos/flexibilidade/evidencias/` | Capturas borradas citadas na coluna `evidencia` das planilhas |

## Verificação do protótipo (M14 e M9)

```bash
pip install playwright            # usa o Google Chrome instalado (canal "chrome")
python coleta/prototipo_mobile.py  # regenera docs/assets/prototipo-mobile/prototipo-interativo.html
python coleta/verificar_prototipo.py [--wave-js caminho/wave.min.js]
```

O protótipo é aberto em modo tela cheia (sem o guia, a moldura e a barra de status simuladas; página inteira rolando e barra de abas fixa) e levado ao estado final de cada tarefa por toques. Sem `--wave-js`, só M14 é medida.

O `wave.min.js` é o motor da extensão oficial WAVE Evaluation Tool (id `jbbplnpkjmmeebjpijfedlgcdilocofh`). Ele pode ser copiado da pasta da extensão instalada no Chrome ou extraído do pacote da Chrome Web Store:

```bash
curl -sL -o wave.crx "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=146.0&acceptformat=crx2,crx3&x=id%3Djbbplnpkjmmeebjpijfedlgcdilocofh%26uc"
unzip -o wave.crx -d wave-ext   # o aviso sobre bytes extras no início é esperado (cabeçalho CRX)
grep version wave-ext/manifest.json   # a coleta de M9 usou a versão 3.3.4.0
```
