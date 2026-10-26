# Gráfico GQM

Os diagramas abaixo representam a hierarquia GQM da avaliação, desdobrando cada objetivo (nível conceitual) em questões (nível operacional) e cada questão em métricas (nível quantitativo). Na visão geral (Figura 1), cada coluna corresponde a um nível do GQM; as Figuras 2 a 4 detalham cada objetivo.

As definições completas estão nas páginas [Objetivos](objetivos.md), [Questões](questoes.md) e [Métricas](metricas.md).

## Visão geral

```mermaid
flowchart LR
    subgraph C["Nível conceitual"]
        G1["G1 - Adequação Funcional"]
        G2["G2 - Capacidade de Interação"]
        G3["G3 - Flexibilidade"]
    end
    subgraph O["Nível operacional"]
        Q1["Q1 - Completude funcional"]
        Q2["Q2 - Correção funcional"]
        Q3["Q3 - Pertinência funcional"]
        Q4["Q4 - Reconhecimento de adequação"]
        Q5["Q5 - Apreensibilidade"]
        Q6["Q6 - Operabilidade (tempo)"]
        Q7["Q7 - Operabilidade (caminho)"]
        Q8["Q8 - Proteção contra erros (recuperação)"]
        Q9["Q9 - Proteção contra erros (tratamento)"]
        Q10["Q10 - Inclusividade (automática)"]
        Q11["Q11 - Inclusividade (manual)"]
        Q12["Q12 - Autodescritividade"]
        Q13["Q13 - Satisfação"]
        Q14["Q14 - Adaptabilidade (software)"]
        Q15["Q15 - Adaptabilidade (hardware: telas e toque)"]
        Q16["Q16 - Adaptabilidade (hardware: esforço no celular)"]
    end
    subgraph Qt["Nível quantitativo"]
        M1["M1 - Cobertura funcional"]
        M2["M2 - Taxa de correção funcional"]
        M3["M3 - Uso de ferramentas externas"]
        M4["M4 - Acerto na primeira escolha"]
        M5["M5 - Conclusão sem ajuda"]
        M6["M6 - Tempo relativo de execução"]
        M7["M7 - Desvio de caminho"]
        M8["M8 - Recuperação de erros"]
        M20["M20 - Cenários de erro tratados"]
        M9["M9 - Erros automáticos de acessibilidade"]
        M10["M10 - Critérios manuais de acessibilidade"]
        M11["M11 - Interpretação sem legenda"]
        M12["M12 - Pontuação SUS"]
        M13["M13 - Compatibilidade entre navegadores"]
        M14["M14 - Páginas adaptadas"]
        M15["M15 - Tempo relativo no celular"]
    end
    G1 --> Q1 & Q2 & Q3
    G2 --> Q4 & Q5 & Q6 & Q7 & Q8 & Q9 & Q10 & Q11 & Q12 & Q13
    G3 --> Q14 & Q15 & Q16
    Q1 --> M1
    Q2 --> M2
    Q3 --> M3
    Q4 --> M4
    Q5 --> M5
    Q6 --> M6
    Q7 --> M7
    Q8 --> M8
    Q9 --> M20
    Q10 --> M9
    Q11 --> M10
    Q12 --> M11
    Q13 --> M12
    Q14 --> M13
    Q15 --> M14
    Q16 --> M15
```

*Figura 1 - Hierarquia GQM da avaliação (visão geral). Fonte: gerado pelo Claude e revisado por Felipe Campêlo (2026); M20 acrescentada e relação questão-métrica 1:1 por Leonardo Bonetti (2026).*

## G1 - Adequação Funcional

```mermaid
flowchart TD
    subgraph C["Nível conceitual"]
        G1["G1: Avaliar a adequação funcional do portal do discente de graduação do SIGAA/UnB, do ponto de vista do estudante de graduação da UnB"]
    end
    subgraph O["Nível operacional"]
        Q1["Q1: O SIGAA oferece as funções de que o estudante precisa?"]
        Q2["Q2: As informações exibidas estão corretas?"]
        Q3["Q3: As funções bastam para planejar o fluxo sem ferramentas externas?"]
    end
    subgraph Qt["Nível quantitativo"]
        M1["M1: Cobertura funcional"]
        M2["M2: Taxa de correção funcional"]
        M3["M3: Proporção de estudantes que usam ferramentas externas"]
    end
    G1 --> Q1 & Q2 & Q3
    Q1 --> M1
    Q2 --> M2
    Q3 --> M3
```

*Figura 2 - Hierarquia GQM do objetivo G1 - Adequação Funcional. Fonte: gerado pelo Claude e revisado por Felipe Campêlo (2026).*

## G2 - Capacidade de Interação (Usabilidade)

```mermaid
flowchart LR
    subgraph C["Nível conceitual"]
        G2["G2: Avaliar a capacidade de interação do portal do discente de graduação do SIGAA/UnB, do ponto de vista do estudante de graduação da UnB"]
    end
    subgraph O["Nível operacional"]
        Q4["Q4: O estudante identifica onde está a função?"]
        Q5["Q5: Conclui as tarefas sem ajuda?"]
        Q6["Q6: Conclui as tarefas sem demora excessiva?"]
        Q7["Q7: Chega à função sem passos desnecessários?"]
        Q8["Q8: Recupera-se quando comete um erro?"]
        Q9["Q9: O sistema trata erros previsíveis?"]
        Q10["Q10: Atende aos critérios verificáveis por ferramenta?"]
        Q11["Q11: Pode ser usado com teclado, leitor de tela e ampliação?"]
        Q12["Q12: Compreende as informações sem legenda?"]
        Q13["Q13: O estudante fica satisfeito?"]
    end
    subgraph Qt["Nível quantitativo"]
        M4["M4: Acerto na primeira escolha de menu"]
        M5["M5: Taxa de conclusão sem ajuda"]
        M6["M6: Tempo relativo de execução"]
        M7["M7: Desvio de caminho"]
        M8["M8: Taxa de recuperação de erros"]
        M20["M20: Cobertura de tratamento de cenários de erro"]
        M9["M9: Erros automáticos de acessibilidade por página"]
        M10["M10: Critérios manuais de acessibilidade atendidos"]
        M11["M11: Interpretação correta sem legenda"]
        M12["M12: Pontuação SUS"]
    end
    G2 --> Q4 & Q5 & Q6 & Q7 & Q8 & Q9 & Q10 & Q11 & Q12 & Q13
    Q4 --> M4
    Q5 --> M5
    Q6 --> M6
    Q7 --> M7
    Q8 --> M8
    Q9 --> M20
    Q10 --> M9
    Q11 --> M10
    Q12 --> M11
    Q13 --> M12
```

*Figura 3 - Hierarquia GQM do objetivo G2 - Capacidade de Interação. Fonte: gerado pelo Claude e revisado por Felipe Campêlo (2026); M20 acrescentada e relação questão-métrica 1:1 por Leonardo Bonetti (2026).*

## G3 - Flexibilidade (Portabilidade)

```mermaid
flowchart TD
    subgraph C["Nível conceitual"]
        G3["G3: Avaliar a flexibilidade do portal do discente de graduação do SIGAA/UnB, do ponto de vista do estudante de graduação da UnB"]
    end
    subgraph O["Nível operacional"]
        Q14["Q14: As tarefas funcionam nos navegadores mais usados?"]
        Q15["Q15: As páginas se adaptam a celular, tablet e toque?"]
        Q16["Q16: O esforço no celular é semelhante ao do computador?"]
    end
    subgraph Qt["Nível quantitativo"]
        M13["M13: Compatibilidade entre navegadores"]
        M14["M14: Páginas adaptadas a telas pequenas e ao toque"]
        M15["M15: Tempo relativo no celular"]
    end
    G3 --> Q14 & Q15 & Q16
    Q14 --> M13
    Q15 --> M14
    Q16 --> M15
```

*Figura 4 - Hierarquia GQM do objetivo G3 - Flexibilidade. Fonte: gerado pelo Claude e revisado por Felipe Campêlo (2026); relação questão-métrica 1:1 por Leonardo Bonetti (2026).*

A métrica auxiliar MA1 não aparece nas figuras porque não responde a uma questão: ela serve apenas para verificar a hipótese de relação HR2 (Tabela 1).

## Matriz de rastreabilidade

A Tabela 1 liga cada característica priorizada na Fase 1 ao objetivo, às questões, às hipóteses e às métricas desta fase. A prioridade indicada é a da [matriz Impacto x Risco](../fase-1/caracteristicas.md#3-caracteristicas-selecionadas).

*Tabela 1 - Rastreabilidade entre característica da Fase 1, objetivo, questão, hipótese e métrica.*

| Característica (Fase 1) | Objetivo | Questão | Hipótese | Métrica |
| ----------------------- | :------: | :-----: | :------: | ------- |
| Adequação Funcional (prioridade 2) | G1 | Q1 | H1 | M1 |
| | | Q2 | H2 | M2 |
| | | Q3 | H3 | M3 |
| Capacidade de Interação (prioridade 1) | G2 | Q4 | H4 | M4 |
| | | Q5 | H5 | M5 |
| | | Q6 | H6 | M6 |
| | | Q7 | H7 | M7 |
| | | Q8 | H8 | M8 |
| | | Q9 | H9 | M20 |
| | | Q10 | H10 | M9 |
| | | Q11 | H11 | M10 |
| | | Q12 | H12 | M11 |
| | | Q13 | H13 | M12 |
| Flexibilidade (prioridade 4) | G3 | Q14 | H14 | M13 |
| | | Q15 | H15 | M14 |
| | | Q16 | H16 | M15 |
| Relações entre as características | - | - | HR1 e HR2 | M5, M6, M14 e M15; métrica auxiliar MA1 |

Cada métrica com nível de pontuação responde a uma única questão, e cada questão tem uma única métrica e uma hipótese com o mesmo número; não há métrica sem questão nem questão sem métrica ou sem hipótese.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 17/10/2026 | Diagramas GQM geral e por objetivo | Felipe Campêlo |
| 1.2 | 18/10/2026 | Numeração e legendas das figuras; nomes das métricas; níveis GQM nas Figuras 2 a 4 | Felipe Campêlo |
| 2.0 | 18/10/2026 | Alinhamento à Fase 1 reestruturada: objetivo G4, questões Q1 a Q14, métricas M1 a M19 e legendas no padrão da Fase 1 | Felipe Campêlo |
| 2.1 | 18/10/2026 | Integração da versão complementar: métrica M20 nas Figuras 1 e 3, nota sobre a métrica auxiliar MA1 e matriz de rastreabilidade Característica, Objetivo, Questão, Hipótese e Métrica | Leonardo Bonetti |
| 2.2 | 25/10/2026 | Remoção do objetivo G4 (Eficiência de Desempenho) da Figura 1, da Figura 5 e da matriz de rastreabilidade; MA1 ligada à HR2 (antiga HR3) | Leonardo Bonetti |
| 2.3 | 25/10/2026 | Objeto dos objetivos nas Figuras 2 a 4: "portal do discente de graduação do SIGAA/UnB" | Leonardo Bonetti |
| 2.4 | 25/10/2026 | Subcaracterística de Q3 nomeada pertinência funcional na Figura 1 | Leonardo Bonetti |
| 2.5 | 25/10/2026 | Ponto de vista dos objetivos nas Figuras 2 a 4: estudante de graduação da UnB | Leonardo Bonetti |
| 2.6 | 25/10/2026 | Figuras 1 a 4 e matriz de rastreabilidade refeitas com a relação questão-métrica 1:1 (Q1 a Q16, H1 a H16) | Leonardo Bonetti |
