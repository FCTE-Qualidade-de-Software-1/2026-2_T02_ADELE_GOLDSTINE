# Uso de IA

Esta página documenta todos os usos de ferramentas de Inteligência Artificial ao longo do projeto, incluindo a finalidade, a data de utilização e o responsável.

## Ferramentas utilizadas

| Ferramenta | Finalidade | Data | Responsável |
| :--------: | :--------: | :--: | :---------: |
| DeepSeek v4 | Estruturação inicial do repositório MkDocs | 16/10/2026 | [Davi Nobre](https://github.com/Jagaima) |
| Claude Opus 5.5 (Claude Code) | Análise do roteiro e do repositório; apoio na redação e formatação da primeira versão da Fase 1. Conteúdo revisado e validado pela equipe | 16/10/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Apoio na redação e formatação da Fase 2 (GQM), com uso de agentes para revisão contra os critérios do roteiro e análise de inconsistências entre as páginas. Conteúdo revisado e validado pela equipe | 17-18/10/2026 | [Felipe Campêlo](https://github.com/felipeacampelo) |
| Claude Opus 5.5 (Claude Code) | Integração da versão complementar à versão de Felipe Campêlo da Fase 2: conversão da numeração, preenchimento de hipóteses e níveis de pontuação, inclusão de M20, MA1, HR1 a HR4 e matriz de rastreabilidade, e verificação de consistência entre as páginas e da compilação do MkDocs. Commits revisados pela equipe antes do envio ao repositório | 18/10/2026 | Leonardo Bonetti |
| Claude Opus 5.5 (Claude Code) | Pesquisa sobre as características de qualidade oficiais e padronizadas (ISO/IEC 25010) e consulta à padronização do IEEE (modelo IEEEtran) para a documentação em LaTeX. Conteúdo revisado pela equipe | 19/10/2026 | [arthurlleite](https://github.com/arthurlleite) |
| Claude Opus 5.5 (Claude Code) | Proposta da metodologia de esforço por horas trabalhadas, *script* de estimativa e cálculo (`gestao/esforco.py`) e reconstrução das horas da Entrega 1 a partir do histórico Git. Taxas e horas fixas revisadas pela equipe | 24/10/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Atualização do artigo em LaTeX após os ajustes da Fase 2 (retirada do objetivo G4) e a inclusão das personas, remoção da capa e do sumário e nova compilação do PDF. Conteúdo conferido com as páginas da GitPage | 25/10/2026 | [arthurlleite](https://github.com/arthurlleite) |
| Claude Opus 5.5 (Claude Code) | Revisão da tabela de contribuição e do *script* de esforço, cálculo da medição 2 dos indicadores PSM a partir do GitHub e apoio na produção dos slides da apresentação de gestão do projeto (Canva). Cada número foi conferido com a planilha, o *script* e o GitHub, e as alterações passam por revisão no PR | 03/11/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Complemento da ata de reuniões com as decisões registradas no repositório (*commits*, PRs, histórico de versões das páginas e retrospectiva) e correção da formatação da ata. Cada data e número foi conferido com o GitHub e com as páginas citadas | 03/11/2026 | Caio Borges |
| Deepseek v4 | Utilização para gerar o gráfico visual em Janela operacional na fase 3, documento cronograma.md | 12/11/2026 | [Davi Nobre](https://github.com/Jagaima) |
| Claude Opus 5.5 (Claude Code) | Revisão das páginas da Fase 3 contra os critérios F3-C1 a F3-C8 e apoio na redação da página Recursos e Ambiente, a partir das fichas das métricas, do escopo da Fase 1 e do protocolo do teste com usuários. Cada recurso foi conferido com a ficha da métrica correspondente, e os itens ainda não decididos ficaram marcados como "a definir" | 12/11/2026 | [Felipe Campêlo](https://github.com/felipeacampelo) |
| Claude Opus 5.5 (Claude Code) | Varredura de consistência depois da integração da Fase 3: busca das páginas que ainda citavam o questionário online, a retenção das gravações e o prazo antigo da Entrega 2, e redação dos ajustes nas Fases 2 e 3 e no cronograma, a partir das decisões da equipe. Cada alteração foi conferida com o protocolo, o termo de consentimento e as fichas das métricas, e passa por revisão no PR | 14/11/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Busca das páginas que restringiam o teste com usuários a estudantes de graduação e redação dos ajustes no protocolo, no questionário, em Recursos e Ambiente, na página Métricas, no escopo da Fase 1 e no termo de consentimento, a partir da decisão da equipe de aceitar estudantes de pós-graduação. Cada alteração foi conferida com o protocolo e o termo, e passa por revisão no PR | 15/11/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Criação do formulário de observação do moderador, a partir das colunas de `sessoes.csv` e `compreensao.csv` e do roteiro do protocolo, e geração em PDF preenchível do questionário SUS e do questionário da Fase 2, com o texto dos itens copiado do protocolo e da página do questionário. Cada página do PDF foi conferida visualmente, e o conteúdo passa por revisão no PR | 15/11/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Análise do comentário do Davi no PR #15 sobre LGPD e guarda dos dados, redação da nova versão do termo de consentimento (LGPD, pseudonimização, transcrição, sessão remota, prazo de guarda do termo e direitos do participante) e ajuste de Recursos e Ambiente e do protocolo. O texto foi conferido com o termo anterior e com a seção 5 de Recursos e Ambiente; o prazo de guarda do termo (60 dias) e o contato (Leonardo) foram decididos pela equipe | 15/11/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Leitura dos PDFs do SUS e do questionário respondidos pelo P1, cálculo da pontuação SUS e transcrição das respostas e das anotações do moderador para `sus.csv`, `respostas.csv`, `sessoes.csv` e `compreensao.csv`, com a proposta de códigos para as respostas do questionário, e primeira passada na gravação (quadros extraídos a cada 0,5 s e cruzados com a transcrição) para medir tempo, cliques e primeira escolha e montar os gabaritos de T2 e T6. Os valores foram conferidos com os PDFs e com o formulário de observação; as medidas da gravação são conferidas por um membro da equipe, que assina como avaliador da gravação, e a classificação dos erros fica com ele | 15/11/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Proposta e implementação dos gráficos do Dashboard de Contribuição (horas por categoria, esforço acumulado e horas por semana) e do tempo de ciclo dos PRs (I4) na Gestão do Projeto, gerados em SVG no build a partir dos mesmos dados do `esforco.py` e da API do GitHub. A paleta foi validada para daltonismo e contraste nos temas claro e escuro, e os gráficos foram conferidos renderizados nos dois temas; cada gráfico tem a tabela com os dados | 15/11/2026 | Caio Borges |
| Claude Opus 5.5 (Claude Code) | Roteiro da sessão em PDF a partir do protocolo, leitura dos PDFs do SUS e do questionário respondidos pelo P3, cálculo da pontuação SUS e transcrição das respostas e das anotações do moderador para `sus.csv`, `respostas.csv`, `sessoes.csv` e `compreensao.csv`, com tempos aproximados tirados da transcrição. Os valores foram conferidos com os PDFs e com o formulário de observação; tempos, cliques, primeira escolha e erros ficam para o avaliador da gravação | 15/11/2026 | [Felipe Campêlo](https://github.com/felipeacampelo) |
| Whisper (modelo medium, pt) | Transcrição automática do áudio da sessão do P3, revisada pelo moderador | 15/11/2026 | [Felipe Campêlo](https://github.com/felipeacampelo) |
| Claude Opus 5.5 (Claude Code) | Escrita dos *scripts* de coleta instrumentada (`coleta/`) que executam T1 a T6 no SIGAA com o Playwright para M13, M14 e os dados complementares de desempenho; execução da coleta na conta de Arthur, que forneceu o acesso; análise dos dados; redação das páginas da Fase 4 (Flexibilidade e Desempenho) e atualização do artigo para o PC2 (Fases 2 a 4, gestão e considerações). Os critérios de M14 foram conferidos nas capturas originais, os casos limítrofes do critério (c) foram decididos por conferência visual, e as afirmações do artigo foram conferidas com os dados brutos e com as páginas da GitPage | 15/11/2026 | [arthurlleite](https://github.com/arthurlleite) |

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação da página de uso de IA | [Davi Nobre](https://github.com/Jagaima) |
| 1.1 | 16/10/2026 | Registro do uso de IA na Fase 1 | Caio Borges |
| 1.2 | 18/10/2026 | Registro do uso de IA na Fase 2 | [Felipe Campêlo](https://github.com/felipeacampelo) |
| 1.3 | 18/10/2026 | Registro do uso de IA na integração das versões da Fase 2 | Leonardo Bonetti |
| 1.4 | 19/10/2026 | Registro do uso de IA na pesquisa das características de qualidade e da padronização IEEE | [arthurlleite](https://github.com/arthurlleite) |
| 1.5 | 24/10/2026 | Registro do uso de IA na metodologia de esforço | Caio Borges |
| 1.6 | 25/10/2026 | Registro do uso de IA na atualização do artigo | [arthurlleite](https://github.com/arthurlleite) |
| 1.7 | 03/11/2026 | Registro do uso de IA na medição 2, na revisão da tabela de contribuição e nos slides de gestão | Caio Borges |
| 1.8 | 03/11/2026 | Registro do uso de IA no complemento da ata de reuniões | Caio Borges |
| 1.9 | 12/11/2026 | Registro do uso de IA na fase 3 | [Davi Nobre](https://github.com/Jagaima) |
| 1.10 | 12/11/2026 | Registro do uso de IA na página Recursos e Ambiente da Fase 3 | [Felipe Campêlo](https://github.com/felipeacampelo) |
| 1.11 | 14/11/2026 | Registro do uso de IA na varredura de consistência das Fases 2 e 3 | Caio Borges |
| 1.12 | 15/11/2026 | Registro do uso de IA na inclusão de estudantes de pós-graduação no teste com usuários | Caio Borges |
| 1.13 | 15/11/2026 | Registro do uso de IA no formulário de observação e nos questionários em PDF | Caio Borges |
| 1.14 | 15/11/2026 | Registro do uso de IA na nova versão do termo de consentimento | Caio Borges |
| 1.15 | 15/11/2026 | Registro do uso de IA na transcrição dos dados do P1 e na primeira passada na gravação | Caio Borges |
| 1.16 | 15/11/2026 | Registro do uso de IA nos gráficos de gestão | Caio Borges |
| 1.17 | 15/11/2026 | Registro do uso de IA na sessão do P3 | [Felipe Campêlo](https://github.com/felipeacampelo) |
| 1.18 | 15/11/2026 | Registro do uso de IA na coleta instrumentada de Flexibilidade e desempenho e na atualização do artigo | [arthurlleite](https://github.com/arthurlleite) |
