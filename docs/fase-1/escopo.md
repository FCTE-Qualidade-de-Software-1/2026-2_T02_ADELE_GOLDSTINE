# Escopo, Profundidade e Rigor da Avaliação

<!-- Critério 6. Nível máximo: muito bem delimitado; racional para cada corte; limites de validade dos resultados. -->

## 1. Objeto da avaliação

O objeto é o **portal do discente de graduação do SIGAA/UnB**, versão v4.15.10.115 (ver [Software Avaliado](software-avaliado.md)), acessado pela **interface web em produção**, durante o 2º semestre letivo de 2026.

## 2. O que será avaliado agora

### 2.1 Tarefas representativas

A avaliação é organizada em torno de tarefas reais do estudante. As tarefas foram escolhidas por **frequência de uso**, **criticidade** para a vida acadêmica e **disponibilidade** durante a janela de coleta.

*Tabela 1 - Tarefas representativas que compõem o escopo.*

| ID | Tarefa | Caminho principal no sistema | Frequência | Criticidade | Características exercitadas |
| :---: | :--- | :--- | :---: | :---: | :--- |
| T1 | Consultar as notas de uma disciplina do semestre | Ensino > Consultar Minhas Notas | Alta | Alta | Cap. Interação, Adequação Funcional, Desempenho, Flexibilidade |
| T2 | Identificar dia, horário e local de uma turma do semestre | Página inicial > Turmas do semestre (código de horário) | Alta | Alta | Cap. Interação (autodescritividade), Adequação Funcional, Flexibilidade |
| T3 | Emitir atestado de matrícula ou histórico escolar | Ensino > Emitir Atestado de Matrícula / Emitir Histórico | Média | Alta | Adequação Funcional, Desempenho, Flexibilidade |
| T4 | Verificar índices acadêmicos e carga horária pendente para a formatura | Ensino > Consultar Índices Acadêmicos / painel de integralização | Média | Alta | Adequação Funcional (completude, correção), Cap. Interação |
| T5 | Acessar um material publicado pelo professor na Turma Virtual | Página inicial > disciplina > Turma Virtual > Materiais | Alta | Média | Cap. Interação (operabilidade), Desempenho, Flexibilidade |
| T6 | Consultar o calendário acadêmico (ex.: prazo de trancamento) | Ensino > Calendário Acadêmico | Média | Média | Cap. Interação (reconhecimento de adequação), Adequação Funcional |

*Fonte: elaboração da equipe.*

### 2.2 Ambientes de execução

*Tabela 2 - Ambientes considerados.*

| Dimensão | Valores considerados |
| :--- | :--- |
| Dispositivos | Computador (desktop/notebook) e celular (Android e iOS) |
| Navegadores | Google Chrome, Mozilla Firefox, Safari e Microsoft Edge, em versões estáveis vigentes |
| Tamanhos de tela | Desktop (>= 1280 px), tablet (cerca de 768 px) e celular (cerca de 360 a 430 px) |
| Rede | Rede doméstica ou institucional e rede móvel simulada (limitação de banda nas ferramentas do navegador) |

*Fonte: elaboração da equipe.*

## 3. Profundidade por característica

*Tabela 3 - Profundidade de avaliação por característica.*

| Característica | Profundidade | Técnicas previstas (detalhadas nas Fases 2 e 3) |
| :--- | :--- | :--- |
| Capacidade de Interação (Usabilidade) | **Alta** | Testes com usuários estudantes sobre as tarefas T1 a T6 (com gravação mediante consentimento), inspeção heurística e verificação automatizada e manual de critérios de acessibilidade |
| Adequação Funcional | **Média** | Roteiro de verificação de funções necessárias por tarefa, conferência de dados exibidos contra documentos oficiais (ex.: histórico x índices) e registro de não conformidades |
| Eficiência de Desempenho | **Média** | Medição do lado do cliente (ferramentas do desenvolvedor, Lighthouse) em horários e redes controlados, com repetição das medidas |
| Flexibilidade (Portabilidade) | **Média** | Execução das tarefas em uma matriz de navegadores e tamanhos de tela, com registro de defeitos de layout e funções inoperantes |

*Fonte: elaboração da equipe.*

A maior profundidade em Capacidade de Interação acompanha a prioridade obtida na [matriz Impacto x Risco](caracteristicas.md#2-avaliacao-das-candidatas).

## 4. O que fica fora do escopo

*Tabela 4 - Itens excluídos e justificativa de cada corte.*

| Item excluído | Justificativa |
| :--- | :--- |
| Portais do docente, do servidor e da coordenação | A equipe não possui credenciais desses perfis e o ponto de vista definido é o do estudante |
| Pós-graduação, ensino a distância e ensino básico/técnico | Funções e regras diferentes da graduação; ampliariam o escopo sem ganho para o propósito |
| Matrícula on-line, ajuste e trancamento | Só ficam disponíveis em períodos definidos pelo calendário, possivelmente fora da janela de coleta; além disso, executá-los alteraria dados acadêmicos reais. Podem ser incluídos por inspeção se o período coincidir com a Fase 4 |
| Módulos de Pesquisa, Extensão, Bolsas, Estágio e Mobilidade | Uso menos frequente e restrito a parte dos estudantes; mantêm o mesmo padrão de interface dos menus avaliados |
| Demais sistemas SIG (SIGRH, SIPAC etc.) | São produtos distintos; a Autenticação Integrada é considerada apenas como passo inicial das tarefas |
| Código-fonte, arquitetura, banco de dados e servidores | Indisponíveis para a equipe (avaliação caixa-preta) |
| Testes de carga, estresse e segurança | Seriam intrusivos em ambiente de produção, sem autorização da STI, e poderiam prejudicar outros usuários |
| Aplicativos de terceiros | Não pertencem ao produto avaliado; são citados apenas como indício de lacunas funcionais |

*Fonte: elaboração da equipe.*

## 5. Limites de validade dos resultados

Os resultados desta avaliação valerão nas seguintes condições:

- **Versão e período:** a versão v4.15.10.115, no 2º semestre de 2026. Atualizações do sistema podem invalidar comparações posteriores.
- **Perfil:** estudantes de graduação, com amostra concentrada na FCTE (campus Gama). A generalização para toda a UnB depende do tamanho e da diversidade da amostra, que serão definidos na Fase 3.
- **Desempenho do lado do cliente:** os tempos medidos incluem rede e navegador e variam com o horário; serão reportados com as condições de medição e não como medidas do servidor.
- **Instância:** os resultados descrevem o SIGAA da UnB, com suas configurações locais; não se estendem automaticamente a outras instituições que usam o produto.
- **Dados reais:** cada participante consulta os próprios dados; diferenças entre históricos acadêmicos podem afetar a comparabilidade de algumas tarefas.

## 6. Premissas e restrições

- Nenhuma tarefa da avaliação altera dados acadêmicos (somente consultas e emissão de documentos).
- A participação de estudantes em testes será voluntária, com termo de consentimento para gravação, conforme a premissa 6 do roteiro.
- Dados pessoais de participantes e de membros da equipe serão anonimizados em todos os artefatos publicados (capturas, planilhas e gravações).
- As medições seguirão protocolos definidos na Fase 3, com registro das condições (data, horário, dispositivo, navegador e rede) para garantir rastreabilidade.

## 7. Rigor da avaliação

O rigor (nível de avaliação) foi definido considerando o risco das decisões apoiadas e os recursos disponíveis:

- **Nível adotado: intermediário.** A avaliação apoia decisões de priorização de melhorias, sem impacto sobre segurança, finanças ou vida; não é uma certificação.
- **Garantias de rigor:** métricas objetivas derivadas pelo método GQM (Fase 2), níveis de pontuação e critérios de julgamento definidos **antes** da coleta, medições repetidas para dados de desempenho, mais de um avaliador nas inspeções e publicação dos dados brutos no repositório.
- **Limitação aceita:** amostra de participantes de conveniência, o que será declarado como ameaça à validade no artigo.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento: objeto, tarefas representativas, ambientes, profundidade, exclusões, limites de validade, premissas e rigor | Caio Borges |
