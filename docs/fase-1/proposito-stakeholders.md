# Propósito da Avaliação e Partes Interessadas

<!-- Critério 1. Nível máximo: propósito claro e alinhado ao contexto; descreve decisões específicas que serão tomadas com a avaliação e quem as tomará. -->
<!-- Critério 2. Nível máximo: mapeamento consistente com critérios de sucesso por stakeholder; mostra influência real nas escolhas. -->

## 1. Propósito da avaliação

### 1.1 Por que avaliar

O SIGAA é o ponto único de acesso do estudante da UnB à sua vida acadêmica: consulta de notas, horários, histórico, emissão de documentos, matrícula, trancamento e acesso às turmas virtuais. Não há alternativa institucional; uma dificuldade no sistema se converte diretamente em atraso, erro de planejamento ou dependência de terceiros.

Há indícios de que o sistema não atende bem esse público:

- a interface foi concebida para uso em computador de mesa, com largura fixa e menus que se abrem ao passar o ponteiro do mouse (ver [Software Avaliado](software-avaliado.md#4-observacoes-preliminares-da-interface));
- informações essenciais são apresentadas em notação codificada, como o horário das turmas ("24M34", "46M5 46T1"), cuja leitura exige consulta a uma legenda;
- estudantes recorrem a ferramentas não oficiais, criadas pela própria comunidade, para tarefas que o sistema não resolve de forma satisfatória, como o planejamento do fluxo de disciplinas até a formatura (por exemplo, o projeto *No Fluxo UnB*).

Esses indícios são, até aqui, percepções. A avaliação existe para **transformar percepções em evidências mensuráveis**, comparáveis a critérios definidos antes da coleta.

### 1.2 Para quem

Os resultados destinam-se, em ordem de prioridade:

1. à **Secretaria de Tecnologia da Informação da UnB (STI/UnB)**, responsável pela operação, configuração e evolução local do SIGAA;
2. ao **Decanato de Ensino de Graduação (DEG)** e às **coordenações de curso**, que orientam os estudantes sobre os procedimentos acadêmicos feitos no sistema;
3. à **comunidade estudantil**, representada por centros acadêmicos, que pode usar os resultados para fundamentar demandas;
4. à **professora da disciplina FGA0315**, na condição de cliente da avaliação, que julga a adequação do processo de avaliação aplicado.

### 1.3 Como os resultados serão usados

*Tabela 1 - Decisões apoiadas pela avaliação.*

| Decisão a ser apoiada | Quem decide | Resultado da avaliação que embasa a decisão |
| :--- | :--- | :--- |
| Quais telas e fluxos do portal do discente priorizar em um ciclo de melhoria | STI/UnB | Ranking das tarefas com pior desempenho em Capacidade de Interação e Adequação Funcional |
| Investir ou não em uma interface responsiva ou aplicativo móvel | STI/UnB | Resultado de Flexibilidade (adaptabilidade a telas e navegadores) cruzado com o perfil de acesso dos estudantes |
| Quais procedimentos precisam de tutorial, aviso ou orientação adicional aos estudantes | DEG e coordenações | Tarefas com maior taxa de erro ou abandono e funções de difícil localização |
| Se há necessidade de otimizar páginas específicas (peso, número de requisições) | STI/UnB | Medidas de comportamento temporal e uso de recursos por página |
| Qual ação de melhoria executar na Fase 4 deste projeto | Equipe avaliadora | Problema de maior impacto entre os julgamentos da Fase 4 |

*Fonte: elaboração da equipe.*

Cenário de aplicação: ao final do semestre, a equipe entrega um relatório com o julgamento de cada característica, as evidências e as oportunidades de melhoria priorizadas. A STI pode usar esse material como insumo para seu planejamento, e a equipe executa, na Fase 4, uma ação de melhoria concreta (por exemplo, um protótipo de alta fidelidade para o fluxo pior avaliado).

## 2. Requisitante e partes interessadas

### 2.1 Requisitante

A avaliação é conduzida pela equipe **Adele Goldstine** (turma T02 de Qualidade de Software 1, FCTE/UnB), que atua como **avaliador independente** (terceira parte): não desenvolve nem opera o SIGAA e não tem acesso a código-fonte ou infraestrutura. A demanda formal da avaliação parte da disciplina FGA0315, que define o processo e os critérios de aceitação do trabalho.

### 2.2 Perfis de usuários considerados

*Tabela 2 - Perfis de estudantes considerados na avaliação.*

| Perfil | Características | Por que importa para a avaliação |
| :--- | :--- | :--- |
| Calouro | Primeiro contato com o sistema; desconhece a terminologia acadêmica (menção, IRA, integralização) | Mede apreensibilidade e reconhecimento de adequação sem conhecimento prévio |
| Veterano | Usa o sistema há vários semestres; já criou atalhos mentais para contornar dificuldades | Serve de contraste: problemas que persistem mesmo com experiência indicam falhas de operabilidade |
| Formando | Precisa conferir integralização, pendências e emitir documentos | Exercita funções de maior criticidade (histórico, índices, carga horária pendente) |
| Estudante que acessa apenas pelo celular | Não dispõe de computador próprio ou o acessa raramente | Exercita a adaptabilidade a telas pequenas e à interação por toque |
| Estudante com deficiência | Usa tecnologias assistivas ou recursos de ampliação | Exercita inclusividade; é considerado de forma inspecional (ver [Escopo](escopo.md)) |

*Fonte: elaboração da equipe.*

### 2.3 Partes interessadas

*Tabela 3 - Partes interessadas, necessidades, critérios de sucesso e influência na avaliação.*

| Parte interessada | Papel em relação ao SIGAA | Necessidade principal | Critério de sucesso | Influência na avaliação |
| :--- | :--- | :--- | :--- | :--- |
| Estudantes de graduação | Usuários finais | Concluir tarefas acadêmicas rapidamente e sem erro, em qualquer dispositivo | Concluir as tarefas de rotina sem ajuda, em tempo aceitável, inclusive no celular | Define o **ponto de vista** da avaliação; justifica Capacidade de Interação, Adequação Funcional e Flexibilidade |
| STI/UnB | Operador e mantenedor local | Saber onde investir esforço de melhoria com o maior retorno | Receber evidências objetivas, rastreáveis e priorizadas | Exige **métricas objetivas** e resultados por tela/tarefa; justifica Eficiência de Desempenho |
| UFRN (desenvolvedora original dos sistemas SIG) | Fornecedora do produto, distribuído a várias instituições | Identificar problemas que afetam todas as instituições usuárias | Problemas descritos de forma reproduzível e independente da instância | Reforça a **descrição do contexto e da versão** avaliada |
| Docentes | Usuários que publicam conteúdo consumido pelos estudantes (notas, notícias, materiais) | Que o estudante encontre o que foi publicado | Estudante localiza materiais e notas sem precisar perguntar | Inclui a **Turma Virtual** no escopo |
| DEG e coordenações de curso | Normatizam e orientam os procedimentos acadêmicos | Reduzir dúvidas e erros recorrentes em procedimentos | Menos solicitações de suporte relacionadas ao uso do sistema | Prioriza tarefas de **emissão de documentos e consulta de índices** |
| Professora da disciplina | Cliente da avaliação | Avaliação conduzida conforme a família SQuaRE, com rastreabilidade | Atendimento aos critérios do roteiro do trabalho final | Determina o **processo** (ISO/IEC 25040) e o **método** (GQM) |

*Fonte: elaboração da equipe.*

A Tabela 3 é retomada na [priorização das características](caracteristicas.md): o peso atribuído ao **impacto** de cada característica considera quais partes interessadas são afetadas por uma deficiência nela.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento: propósito, decisões apoiadas, perfis de usuários e partes interessadas | Caio Borges |
