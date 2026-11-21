# Acessibilidade Automática (M9): execução e resultados

<!-- Critérios F4-C1 a F4-C3: execução conforme o plano da Fase 3, dados brutos rastreáveis, cálculo de M9 e resposta a Q10/H10. -->

Esta página registra a execução e os resultados da métrica **M9 (erros automáticos de acessibilidade por página)**, vinculada à subcaracterística **inclusividade** do objetivo **G2 - Capacidade de Interação (Usabilidade)**. A verificação complementar por inspeção manual (M10 — teclado, foco visível, ampliação a 200% e leitor de tela) depende de dois avaliadores independentes e segue pendente.

## 1. Rastreabilidade

*Tabela 1 - Da característica ao arquivo de dados (M9).*

| Nível | Especificação |
| ----- | ------------- |
| Característica (ISO/IEC 25010:2023) [1] | Capacidade de Interação (Usabilidade), subcaracterística **inclusividade** |
| Referência normativa de acessibilidade | WCAG 2.2, critérios verificáveis automaticamente nos níveis A e AA [2] |
| Objetivo, questão e hipótese ([Fase 2](../fase-2/hipoteses.md)) | G2; Q10; H10: M9 > 5 erros por página (Insatisfatório) |
| Ficha da métrica | [M9 - Erros automáticos de acessibilidade por página](../fase-2/metricas.md#m9-erros-automaticos-de-acessibilidade-por-pagina) |
| Instrumento | Motor oficial da extensão WAVE Evaluation Tool (WebAIM) v3.3.4.0 [3], executada no Google Chrome |
| Relatórios brutos | `dados/brutos/acessibilidade/wave/T1-wave.json` a `T6-wave.json` |
| Planilha de resumo | `dados/brutos/acessibilidade/wave/resumo.csv` |
| Valor consolidado | `dados/consolidados/metricas.csv` |

*Fonte: elaboração da equipe.*

## 2. Método e ambiente de coleta

O plano da Fase 3 ([Recursos e Ambiente](../fase-3/recursos-ambiente.md#2-hardware-e-software-por-metodo)) especifica a execução da extensão **WAVE (WebAIM)** no Google Chrome, em computador com tela de pelo menos 1280 px, sobre a página final de cada tarefa T1 a T6 com o estudante autenticado.

Para tornar a coleta repetível e auditável, o *script* [`coleta/coleta_wave.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/coleta/coleta_wave.py) reutiliza a navegação autenticada de `coleta/sigaa_coleta.py`, chega à página final de cada tarefa no Google Chrome real e injeta o motor oficial da extensão **WAVE Evaluation Tool v3.3.4.0** (`wave.min.js`), capturando o objeto estruturado de resultados emitido pelo evento `waveResults`. Antes da gravação dos arquivos `T1-wave.json` a `T6-wave.json`, o *script* remove qualquer trecho de texto das páginas, mantendo apenas os códigos de regra do WAVE, as descrições oficiais das regras e as contagens de ocorrências — protegendo os dados pessoais da conta do avaliador conforme a premissa 5 do roteiro.

*Tabela 2 - Ambiente da coleta de M9.*

| Item | Especificação |
| ---- | ------------- |
| Data e horário | 21/11/2026, das 15h56 às 15h58 (horário de Brasília) |
| Avaliador | Felipe Campêlo (1 avaliador, conforme a [Tabela 4 de Recursos e Ambiente](../fase-3/recursos-ambiente.md#3-pessoas-e-conhecimento-exigido)) |
| Produto | Portal do Discente do SIGAA/UnB **v4.15.10.116**, conferida no rodapé das páginas que exibem a versão (T2, T5 e T6) |
| Navegador e sistema | Google Chrome 157.0.8103.79 estável, em janela de 1366 × 768 px, macOS (Darwin 25.6.0) |
| Ferramenta | Motor oficial da extensão WAVE Evaluation Tool v3.3.4.0 (WebAIM) |
| Conta | Conta de estudante de graduação de Felipe Campêlo; em T5, página de visualização de notícia da turma *Técnicas de Programação em Plataformas Emergentes* (mesmo recorte registrado em [Flexibilidade](flexibilidade.md#7-desvios-em-relacao-ao-plano-da-fase-3-e-ameacas-a-validade)) |

*Fonte: elaboração da equipe; valores registrados em `dados/brutos/acessibilidade/wave/T*-wave.json`.*

**Critério de contagem de erros:** a ficha de M9 especifica contar *"apenas os itens classificados como erro, não os alertas"*, abrangendo os **níveis A e AA das WCAG 2.2**. Na taxonomia do WAVE, erros de nível A aparecem na categoria *Errors* (`error`) e erros de contraste de nível AA (WCAG 1.4.3) aparecem na categoria *Contrast Errors* (`contrast`). Por isso, o total de erros de cada página soma `error + contrast`, enquanto *Alerts* (`alert`) são registrados em `resumo.csv` sem entrar no cálculo da métrica. Como verificação de sensibilidade, a seção 3 apresenta também o valor contando apenas `error` (sem contraste) e apenas elementos visíveis no DOM.

## 3. Resultados por página e por tipo de erro

*Tabela 3 - Resultado de M9 por página analisada.*

| Tarefa | Página analisada | Erros gerais (WCAG A) | Erros de contraste (WCAG AA) | Total de erros | Nível da página (regra 3) | Alertas (fora da métrica) | Elementos DOM | Relatório |
| :----: | ---------------- | :-------------------: | :--------------------------: | :------------: | ------------------------- | :-----------------------: | :-----------: | --------- |
| T1 | Relatório de notas do aluno | 4 | 0 | **4** | Regular | 307 | 466 | [`T1-wave.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/acessibilidade/wave/T1-wave.json) |
| T2 | Portal do Discente (Turmas do Semestre) | 22 | 0 | **22** | Insatisfatório | 232 | 1.264 | [`T2-wave.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/acessibilidade/wave/T2-wave.json) |
| T3 | Atestado de matrícula | 3 | 0 | **3** | Regular | 87 | 265 | [`T3-wave.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/acessibilidade/wave/T3-wave.json) |
| T4 | Índices acadêmicos | 11 | 0 | **11** | Insatisfatório | 14 | 274 | [`T4-wave.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/acessibilidade/wave/T4-wave.json) |
| T5 | Turma Virtual (notícia da turma) | 35 | 2 | **37** | Insatisfatório | 46 | 796 | [`T5-wave.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/acessibilidade/wave/T5-wave.json) |
| T6 | Calendário acadêmico 2026.2 | 1 | 1 | **2** | Bom | 9 | 252 | [`T6-wave.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/acessibilidade/wave/T6-wave.json) |
| **Total / Média** | **6 páginas** | **76** | **3** | **79 (média 13,17)** | **Insatisfatório** | **695** | **3.317** | [`resumo.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/brutos/acessibilidade/wave/resumo.csv) |

*Fonte: `dados/brutos/acessibilidade/wave/resumo.csv` e relatórios `T1-wave.json` a `T6-wave.json`.*

**Valor de M9:** A = 79 erros detectados em B = 6 páginas analisadas. **M9 = 79 / 6 = 13,17 erros por página**, nível **Insatisfatório** (faixa > 5 erros por página na Tabela 3 de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#metricas-em-que-valores-menores-sao-melhores)).

**Análise de sensibilidade:** mesmo sob critérios mais restritivos de contagem, o nível de M9 não muda:

- **Sem erros de contraste** (apenas a categoria *Errors* do WAVE): 76 / 6 = **12,67 erros/página** (Insatisfatório).
- **Apenas elementos visíveis no DOM** (excluindo 34 ocorrências em elementos marcados como `hidden` pelo WAVE, sobretudo em diálogos ocultos de T4 e T5): 45 / 6 = **7,50 erros/página** (Insatisfatório).

*Tabela 4 - Distribuição dos 79 erros detectados pelo WAVE por regra e critério WCAG 2.2.*

| Código WAVE | Descrição oficial | Categoria | Critério WCAG 2.2 | T1 | T2 | T3 | T4 | T5 | T6 | Total | % |
| ----------- | ----------------- | --------- | ----------------- | :-: | :-: | :-: | :-: | :-: | :-: | :---: | :-: |
| `alt_missing` | *Missing alternative text* | Error | 1.1.1 (A) | 3 | 16 | 2 | 8 | 18 | 0 | **47** | 59,5% |
| `button_empty` | *Empty button* | Error | 1.1.1 / 2.4.4 (A) | 0 | 0 | 0 | 2 | 9 | 0 | **11** | 13,9% |
| `language_missing` | *Language missing or invalid* | Error | 3.1.1 (A) | 1 | 1 | 1 | 1 | 1 | 1 | **6** | 7,6% |
| `th_empty` | *Empty table header* | Error | 1.3.1 (A) | 0 | 4 | 0 | 0 | 1 | 0 | **5** | 6,3% |
| `label_missing` | *Missing form label* | Error | 1.1.1 / 1.3.1 / 3.3.2 (A) | 0 | 0 | 0 | 0 | 3 | 0 | **3** | 3,8% |
| `link_empty` | *Empty link* | Error | 2.4.4 (A) | 0 | 0 | 0 | 0 | 3 | 0 | **3** | 3,8% |
| `contrast` | *Very low contrast* | Contrast Error | 1.4.3 (AA) | 0 | 0 | 0 | 0 | 2 | 1 | **3** | 3,8% |
| `alt_input_missing` | *Image button missing alternative text* | Error | 1.1.1 / 2.4.4 (A) | 0 | 1 | 0 | 0 | 0 | 0 | **1** | 1,3% |
| **Total** | | | | **4** | **22** | **3** | **11** | **37** | **2** | **79** | **100,0%** |

*Fonte: `dados/brutos/acessibilidade/wave/T1-wave.json` a `T6-wave.json`.*

**O que os dados revelam:** os erros não são isolados nem dependentes do conteúdo de uma única conta; eles decorrem da arquitetura de interface legada (JSF/RichFaces) do SIGAA:

- **Falta de texto alternativo (`alt_missing` e `alt_input_missing`) responde por 60,8% dos erros (48 de 79):** ícones de ação, imagens decorativas e botões baseados em imagem são renderizados sem atributo `alt`, o que faz leitores de tela anunciarem nomes de arquivo ou omitirem o propósito do controle.
- **Nenhuma página declara o idioma do documento (`language_missing` em 6 de 6 páginas):** a ausência de `lang="pt-BR"` na raiz `<html>` impede que leitores de tela selecionem automaticamente a pronúncia em português e impede que qualquer página do escopo atinja o nível Excelente (0 erros).
- **Concentração nas telas mais usadas:** a **Turma Virtual (T5, 37 erros)** e o **Portal do Discente (T2, 22 erros)** concentram **74,7% (59 de 79)** de todos os erros automáticos, justamente as duas telas pelas quais o estudante passa com maior frequência. Apenas T5 usa atributos ARIA (18 ocorrências), mas ainda assim reúne botões vazios (`button_empty`), links vazios (`link_empty`) e campos sem rótulo (`label_missing`).
- **Baixo número de erros de contraste automático (3 de 79):** o contraste de cores não é o principal gargalo automático (apenas 2 ocorrências em T5 e 1 em T6), embora a paleta antiga ainda gere 695 alertas de estrutura, redundância de texto e tabelas de layout (com pico de 307 alertas em T1 e 232 em T2).

## 4. Julgamento de Q10 e classificação de H10

*Tabela 5 - Julgamento de Q10 e classificação de H10.*

| Questão | Métrica | Valor | Nível da questão | Hipótese | Classificação |
| :-----: | :-----: | :---: | ---------------- | -------- | ------------- |
| Q10 | M9 | 13,17 erros/página (79 erros em 6 páginas) | **Insatisfatório (0)** | H10: M9 > 5 erros por página (Insatisfatório) | **Confirmada** |

*Fonte: elaboração da equipe, pelas regras de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#criterios-de-julgamento).*

**Resposta a Q10** (Tabela 4 de Níveis de Pontuação, nível Insatisfatório): **Não.** As páginas do escopo não atendem aos critérios de acessibilidade verificáveis automaticamente nas WCAG 2.2 (níveis A e AA): a média de 13,17 erros por página supera em mais de duas vezes e meia o limite do nível Insatisfatório (5 erros/página), e todas as seis páginas apresentam ao menos a falta de declaração de idioma.

**Classificação de H10:** **Confirmada.** A hipótese previa erros automáticos frequentes (> 5 por página) associados à interface JSF com muitos elementos sem rótulo ou texto alternativo, padrão observado diretamente nas seis páginas.

**Impacto sobre G2 (Capacidade de Interação):** como a avaliação automática detecta apenas um subconjunto das barreiras de acessibilidade, 13,17 erros por página representa um limite inferior para os problemas de inclusividade (a ser complementado por M10). Pelas regras de julgamento da Fase 2 (Tabela 6 de Níveis de Pontuação), a presença de uma questão Insatisfatória (Q10) já impede que Capacidade de Interação receba os julgamentos *Atende* ou *Atende plenamente*.

## 5. Desvios em relação ao plano e ameaças à validade

*Tabela 6 - Desvios do plano e limitações da coleta de M9.*

| Aspecto | O que foi feito | Efeito e tratamento |
| ------- | --------------- | ------------------- |
| Acionamento da extensão WAVE | Injeção do motor oficial da extensão WAVE Evaluation Tool v3.3.4.0 (`wave.min.js`) via Playwright no Google Chrome 157, em vez de clique manual no ícone da barra do navegador | Executa exatamente o mesmo código de avaliação da extensão oficial instalada pela Chrome Web Store, garantindo repetibilidade e exportação sanitizada sem textos pessoais |
| Página final de T5 | Página de visualização de notícia na Turma Virtual de *Técnicas de Programação em Plataformas Emergentes* | Mesma adaptação da coleta de M13 (nenhuma turma da conta tinha arquivo anexado). A estrutura de menu, cabeçalho e diálogos da Turma Virtual é a mesma das demais telas do módulo |
| Elementos ocultos no DOM | O WAVE contabiliza erros em elementos ocultos (ex.: diálogos JSF presentes no HTML da Turma Virtual e de Índices) | Os relatórios JSON registram `hidden_count` por regra; mesmo excluindo todos os 34 erros ocultos, a média permanece em 7,50 erros/página (Insatisfatório) |
| Limite da verificação automática | Ferramentas automáticas não avaliam ordem de foco, operação integral por teclado nem qualidade do anúncio em leitor de tela | M9 funciona como limite inferior; a avaliação completa da subcaracterística inclusividade depende de M10 |

*Fonte: elaboração da equipe.*

## 6. Como reproduzir

Os passos estão em [`coleta/README.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/coleta/README.md). Com o arquivo `wave.min.js` da extensão oficial WAVE Evaluation Tool disponível localmente e as variáveis `SIGAA_USUARIO` e `SIGAA_SENHA` definidas:

```bash
python coleta/coleta_wave.py --wave-js /caminho/para/wave.min.js --avaliador Felipe
python coleta/calcular.py
```

## Referências

[1] ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

[2] W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>.

[3] WEBAIM. *WAVE Web Accessibility Evaluation Tool* (versão 3.3.4.0). Utah State University, 2026. Disponível em: <https://wave.webaim.org/>. Acesso em: 21 nov. 2026.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 21/11/2026 | Execução automatizada de M9 com o motor oficial do WAVE v3.3.4.0 nas páginas de T1 a T6, análise por regra WCAG 2.2, julgamento de Q10 e confirmação de H10 | [Felipe Campêlo](https://github.com/felipeacampelo) |
