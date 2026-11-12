# Recursos e Ambiente da Avaliação

Esta página especifica o que é necessário para executar a avaliação na Fase 4: o produto e a versão avaliados, o hardware e o software de cada método de coleta, as pessoas e o conhecimento exigido delas, a massa de dados e o tratamento das gravações. O ambiente das sessões do teste com usuários já está no [Protocolo do Teste com Usuários](teste-usuarios.md#3-ambiente-e-materiais) e não é repetido aqui; esta página cobre os demais métodos e os recursos comuns a todos.

## 1. Produto avaliado

*Tabela 1 - Produto avaliado.*

| Item | Especificação |
| ---- | ------------- |
| Sistema | Portal do discente de graduação do SIGAA/UnB, versão v4.15.10.115, conforme o [objeto da avaliação](../fase-1/escopo.md#1-objeto-da-avaliacao) |
| Acesso | Interface web em produção, com a conta institucional de um estudante de graduação ativo |
| Tipo de avaliação | Caixa-preta, só por consultas e emissão de documentos, sem alteração de dados acadêmicos ([premissas da Fase 1](../fase-1/escopo.md#6-premissas-e-restricoes)) |
| Controle de versão | A versão exibida no rodapé do SIGAA é conferida no primeiro dia de coleta e em cada dia seguinte. Se mudar durante a Fase 4, a mudança e a data são registradas na página de resultados, e as medidas obtidas antes e depois são identificadas |

*Fonte: elaboração da equipe.*

## 2. Hardware e software por método

A Tabela 2 lista os recursos de cada método de coleta da [Tabela 2 da Fase 3](index.md#31-metodos-de-coleta). Nas versões estáveis de navegadores e ferramentas, a versão exata é a vigente no dia da coleta e fica registrada em cada linha dos arquivos de dados (colunas `navegador`, `versao` e `data` das [Planilhas de Coleta](planilhas.md)).

*Tabela 2 - Recursos por método de coleta.*

| Método | Métricas | Hardware | Software |
| ------ | -------- | -------- | -------- |
| Teste com usuários | M4, M5, M6, M7, M8, M11, M12 e MA1 | Ver [Protocolo do Teste com Usuários](teste-usuarios.md#3-ambiente-e-materiais) | Ver [Protocolo do Teste com Usuários](teste-usuarios.md#3-ambiente-e-materiais) |
| Tempos do especialista | M6 | O mesmo computador das sessões, para que T<sub>e</sub> e T<sub>p</sub> sejam medidos nas mesmas condições | Google Chrome, nas mesmas configurações das sessões; gravador de tela |
| Questionário online | M3 e lista de referência de M1 | Nenhum específico | Google Forms, sem coleta de e-mail, conforme o [Questionário](../fase-2/questionario.md#1-caracteristicas-do-instrumento); exportação em CSV |
| Inspeção de funções e de correção | M1 e M2 | Computador com tela de pelo menos 1280 px | Navegador da escolha do avaliador; documentos oficiais da Seção 4.2 |
| Cenários de erro | M20 | Computador com tela de pelo menos 1280 px | Google Chrome; bloqueador de janelas no padrão do navegador, para o cenário C6 |
| Acessibilidade automática | M9 | Computador com tela de pelo menos 1280 px | Extensão WAVE (WebAIM) no Google Chrome |
| Acessibilidade manual | M10 | Computador com teclado físico | Leitor de tela NVDA com Chrome ou Firefox no Windows, ou VoiceOver com Safari no macOS; zoom do próprio navegador (200%) |
| Compatibilidade entre navegadores | M13 | Um computador com macOS, necessário para o Safari, e um computador com Windows ou macOS para os demais | Google Chrome, Mozilla Firefox, Microsoft Edge e Safari, nas versões estáveis vigentes |
| Adaptação a telas pequenas e ao toque | M14 | Celular real com tela de cerca de 360 px de largura; computador para a verificação em 768 px | No celular, o navegador padrão do aparelho. Em 768 px, o modo de dispositivo das ferramentas do desenvolvedor do Chrome, com emulação de toque, ou um tablet real |
| Tempo relativo no celular | M15 | O mesmo celular de M14 e um computador com tela de pelo menos 1280 px | Gravação de tela nativa do celular (Android ou iOS) e gravador de tela no computador |

*Fonte: elaboração da equipe.*

**Celulares:** os aparelhos usados em M14 e M15 ainda serão definidos pela equipe. A Tabela 3 é preenchida antes da primeira coleta, e o mesmo aparelho é usado em M14 e M15 para que os dois resultados possam ser comparados.

*Tabela 3 - Celulares usados na coleta.*

| Aparelho | Sistema e versão | Largura da área de exibição (px) | Navegador | Avaliador |
| -------- | ---------------- | :------------------------------: | --------- | --------- |
| A definir | A definir | A definir | A definir | A definir |

*Fonte: elaboração da equipe.*

**Gravador de tela:** no macOS, o gravador nativo (Cmd + Shift + 5), com a opção "Mostrar cliques do mouse" ligada; no Windows, o OBS Studio. A marcação dos cliques facilita a contagem de M7, como pede o [protocolo](teste-usuarios.md#3-ambiente-e-materiais).

**Rede:** a rede usada é registrada em cada linha dos arquivos de dados que a pedem. As métricas mantidas na Fase 2 não dependem de limitação de banda, que a [Tabela 2 do escopo da Fase 1](../fase-1/escopo.md#22-ambientes-de-execucao) previa para as medidas de desempenho. Em M15, computador e celular usam a mesma rede, conforme a ficha da métrica.

## 3. Pessoas e conhecimento exigido

*Tabela 4 - Papéis, quantidade e conhecimento exigido.*

| Papel | Quantidade | Conhecimento em informática | Conhecimento do domínio (SIGAA e vida acadêmica) | Preparação antes da coleta |
| ----- | :--------: | --------------------------- | ------------------------------------------------ | -------------------------- |
| Participante do teste com usuários | 6, mais 2 reservas | Uso básico de computador e navegador | Variável por grupo, de propósito: calouros do 1º ou 2º semestre e estudantes a partir do 5º semestre ([Protocolo](teste-usuarios.md#1-participantes)) | Nenhuma. O participante não recebe treinamento nem explicação do sistema |
| Respondente do questionário | Ao menos 60 | Uso básico de formulário online | Estudante de graduação ativo da UnB | Nenhuma |
| Moderador | 1 por sessão | Uso de gravador de tela | Conhecer as tarefas T1 a T6 e os enunciados | Leitura do protocolo e participação na sessão piloto |
| Avaliador da gravação | 1 por sessão, de preferência diferente do moderador | Leitura de vídeo com marcação de tempo | Conhecer os caminhos de `caminhos.csv` e as definições comuns de [Métricas](../fase-2/metricas.md#definicoes-comuns) | Leitura da seção 8 do protocolo |
| Especialista (M6) | 1 | Uso fluente do navegador | Uso frequente do SIGAA; executar as tarefas pelo caminho mais curto sem hesitar | Ensaiar cada tarefa antes das três execuções medidas |
| Avaliador de inspeção | 2 independentes, mais 1 para desempate, nas métricas cuja ficha o exige (M1, M2, M10 e M20); 1 nas demais | Ferramentas do desenvolvedor do navegador (M14); extensão WAVE (M9); leitor de tela e navegação só por teclado (M10) | Estudante da UnB com acesso ao SIGAA; para M2, leitura do PPC e do calendário acadêmico | Leitura da ficha da métrica. Para M10, cerca de 30 minutos de prática com o leitor de tela fora do SIGAA, porque nenhum membro da equipe o usa no dia a dia |

*Fonte: elaboração da equipe.*

Os avaliadores de inspeção são membros da equipe e, portanto, estudantes de engenharia de software com mais familiaridade com informática do que o estudante médio. Isso não afeta as métricas de inspeção, que verificam critérios objetivos das fichas, mas é o motivo de as métricas de esforço do estudante (M4 a M8 e M11) virem do teste com usuários, e não da equipe. A distribuição dos papéis entre os membros fica no cronograma da avaliação.

## 4. Massa de dados

O SIGAA da UnB não tem ambiente de testes acessível à equipe, e a avaliação é de caixa-preta em produção. Por isso, a massa de dados são as **contas reais** dos estudantes: as de membros da equipe nas inspeções e a do próprio participante no teste com usuários. Não é criado nem alterado nenhum dado acadêmico.

### 4.1 Requisitos de cada conta

Para que as tarefas possam ser executadas, a conta usada precisa ter os dados da Tabela 5. Sem eles, a tarefa não é possível e a medida não reflete o sistema, e sim a falta de dados.

*Tabela 5 - Dados necessários na conta para cada tarefa.*

| Tarefa | Dado necessário na conta | Por que é necessário | Como é conferido |
| ------ | ------------------------ | -------------------- | ---------------- |
| T1 | Ao menos uma nota lançada em disciplina do semestre corrente | Sem nota, a página de notas não mostra o que a tarefa pede | Pergunta no recrutamento; sessão piloto |
| T2 | Matrícula em ao menos uma turma do semestre com horário e local cadastrados | A tarefa e a pergunta de compreensão dependem do código de horário | Pergunta no recrutamento |
| T3 | Vínculo ativo no semestre corrente | Sem vínculo, o atestado não é emitido | Critério de inclusão do protocolo |
| T4 | Índices acadêmicos e integralização calculados | Calouros do 1º semestre podem ainda não ter índices, conforme a [sessão piloto](teste-usuarios.md#10-sessao-piloto) | Sessão piloto e conferência na conta de um calouro antes da coleta |
| T5 | Ao menos um material publicado por professor na Turma Virtual de uma turma do semestre | Sem material, não há o que abrir | Pergunta no recrutamento |
| T6 | Calendário acadêmico do semestre publicado | A pergunta de compreensão usa o prazo de trancamento | Conferência pela equipe antes da coleta |

*Fonte: elaboração da equipe.*

Nas inspeções (M1, M2, M9, M10, M13, M14, M15 e M20), cada avaliador usa a própria conta, que precisa atender aos mesmos requisitos. As páginas inspecionadas são as páginas finais de T1 a T6, as mesmas em todas as métricas, para que os resultados por tarefa possam ser comparados (regra 3 de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#regra-3-resultados-por-perfil-por-pagina-e-por-tarefa)).

### 4.2 Fontes oficiais para M2

M2 compara o que o SIGAA exibe com fontes externas a ele. As fontes são reunidas antes da coleta e guardadas na mesma data, porque podem mudar durante o semestre.

*Tabela 6 - Fontes oficiais de comparação.*

| Fonte | Usada para conferir |
| ----- | ------------------- |
| Calendário acadêmico do semestre publicado no site da UnB | Datas exibidas em T6 |
| Projeto Pedagógico do Curso (PPC) do avaliador | Carga horária total e por tipo de componente em T4 |
| Histórico escolar e atestado emitidos pelo próprio SIGAA | Coerência com as informações das telas de T1, T3 e T4 |

*Fonte: elaboração da equipe.*

### 4.3 Proteção dos dados pessoais

As contas reais exibem nome, matrícula, notas e histórico. Por isso:

- capturas de tela publicadas no repositório têm nome, matrícula, foto e notas cobertos antes do envio;
- os arquivos de dados identificam participantes só pelo código (P1 a P6) e avaliadores só pelo primeiro nome, conforme as [convenções das planilhas](planilhas.md#1-convencoes);
- documentos emitidos em T3 durante o teste são apagados ao fim de cada sessão, como prevê o roteiro do protocolo.

## 5. Gravações

A Fase 2 deixou para esta fase a definição do acesso às gravações ([Artefatos de dados previstos](../fase-2/metricas.md#artefatos-de-dados-previstos)). As gravações das sessões mostram a tela do SIGAA com dados acadêmicos do participante e a voz dele. Por isso não são publicadas no repositório, que é público.

*Tabela 7 - Guarda e acesso às gravações.*

| Item | Definição |
| ---- | --------- |
| Local | Pasta em um drive compartilhado da equipe, com acesso restrito (local definitivo a confirmar pela equipe) |
| Quem acessa | Membros da equipe e a professora da disciplina |
| Nome dos arquivos | `Entrevista_<número>_<nome>`, por exemplo `Entrevista_3_Maria`. O número é o mesmo do código do participante (`Entrevista_3` corresponde a P3). Como o nome só aparece na pasta restrita, o repositório usa apenas o código |
| Consentimento | Registrado antes de qualquer gravação, conforme o [roteiro do protocolo](teste-usuarios.md#5-roteiro-da-sessao). O registro de cada participante fica na mesma pasta restrita |
| Ligação com o repositório | No repositório, os dados extraídos das gravações (tempos, cliques, primeira escolha e erros) apontam para o minuto do vídeo na coluna `evidencia` (ex.: `P3 04:12`). O link da pasta é informado à professora junto com a release da Entrega 2 |
| Retenção | Até a publicação das menções finais da disciplina. Depois, as gravações são apagadas |

*Fonte: elaboração da equipe.*

As gravações das execuções de M15 e dos tempos do especialista são feitas por membros da equipe com as próprias contas e seguem as mesmas regras.

## 6. Coerência com a Fase 2

A Tabela 8 mostra como os recursos especificados atendem ao que as fichas das métricas e os [Níveis de Pontuação](../fase-2/niveis-pontuacao.md) exigem para que cada resultado possa ser julgado.

*Tabela 8 - Recurso especificado e exigência da Fase 2.*

| Exigência da Fase 2 | Recurso que a atende |
| ------------------- | -------------------- |
| M13 tem 24 combinações (6 tarefas × 4 navegadores) | Computador com macOS para o Safari e os outros três navegadores (Tabela 2) |
| M14 tem 12 verificações (6 páginas × 2 larguras) | Celular real de cerca de 360 px e modo de dispositivo ou tablet em 768 px (Tabelas 2 e 3) |
| M15 compara o mesmo avaliador no computador e no celular | O mesmo celular de M14, a mesma rede e gravação de tela nos dois aparelhos (Seção 2) |
| M6 compara participantes com um especialista | O especialista usa o computador e o navegador das sessões (Tabela 2) |
| M10 exige teclado, zoom de 200% e leitor de tela | NVDA ou VoiceOver, teclado físico e prática prévia dos avaliadores (Tabelas 2 e 4) |
| M1, M2, M10 e M20 exigem dois avaliadores independentes e um terceiro para divergências | Três membros com conta que atenda à Tabela 5 (Tabela 4) |
| A regra 3 dos níveis exige ao menos três participantes por grupo | Seis participantes e duas reservas (Tabela 4) |
| As tarefas T1 a T6 precisam ser possíveis na conta usada | Requisitos de conta da Tabela 5, conferidos no recrutamento e na sessão piloto |

*Fonte: elaboração da equipe.*

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 12/11/2026 | Criação da página: produto avaliado, hardware e software por método, pessoas e conhecimento exigido, massa de dados, gravações e coerência com a Fase 2 | [Felipe Campêlo](https://github.com/felipeacampelo) |
