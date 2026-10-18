# Gráfico GQM

Os diagramas abaixo representam a hierarquia GQM da avaliação, desdobrando cada objetivo (nível conceitual) em questões (nível operacional) e cada questão em métricas (nível quantitativo). Na visão geral (Figura 1), cada coluna corresponde a um nível do GQM; as Figuras 2 a 5 detalham cada objetivo.

As definições completas estão nas páginas [Objetivos](objetivos.md), [Questões](questoes.md) e [Métricas](metricas.md).

## Visão geral

```mermaid
flowchart LR
    subgraph C["Nível conceitual"]
        G1["G1 - Adequação Funcional"]
        G2["G2 - Capacidade de Interação"]
        G3["G3 - Flexibilidade"]
        G4["G4 - Eficiência de Desempenho"]
    end
    subgraph O["Nível operacional"]
        Q1["Q1 - Completude funcional"]
        Q2["Q2 - Correção funcional"]
        Q3["Q3 - Adequação funcional (pertinência)"]
        Q4["Q4 - Reconhecimento de adequação"]
        Q5["Q5 - Apreensibilidade"]
        Q6["Q6 - Operabilidade"]
        Q7["Q7 - Proteção contra erros"]
        Q8["Q8 - Inclusividade"]
        Q9["Q9 - Autodescritividade"]
        Q10["Q10 - Satisfação"]
        Q11["Q11 - Adaptabilidade (software)"]
        Q12["Q12 - Adaptabilidade (hardware)"]
        Q13["Q13 - Comportamento temporal"]
        Q14["Q14 - Utilização de recursos"]
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
        M9["M9 - Erros automáticos de acessibilidade"]
        M10["M10 - Critérios manuais de acessibilidade"]
        M11["M11 - Interpretação sem legenda"]
        M12["M12 - Pontuação SUS"]
        M13["M13 - Compatibilidade entre navegadores"]
        M14["M14 - Páginas adaptadas"]
        M15["M15 - Tempo relativo no celular"]
        M16["M16 - LCP em rede comum"]
        M17["M17 - LCP em rede móvel"]
        M18["M18 - Peso por página"]
        M19["M19 - Requisições por página"]
    end
    G1 --> Q1 & Q2 & Q3
    G2 --> Q4 & Q5 & Q6 & Q7 & Q8 & Q9 & Q10
    G3 --> Q11 & Q12
    G4 --> Q13 & Q14
    Q1 --> M1
    Q2 --> M2
    Q3 --> M3
    Q4 --> M4
    Q5 --> M5
    Q6 --> M6 & M7
    Q7 --> M8
    Q8 --> M9 & M10
    Q9 --> M11
    Q10 --> M12
    Q11 --> M13
    Q12 --> M14 & M15
    Q13 --> M16 & M17
    Q14 --> M18 & M19
```

*Figura 1 - Hierarquia GQM da avaliação (visão geral). Fonte: gerado pelo Claude e revisado por Felipe Campêlo (2026).*

## G1 - Adequação Funcional

```mermaid
flowchart TD
    subgraph C["Nível conceitual"]
        G1["G1: Avaliar a adequação funcional do portal do discente do SIGAA/UnB, do ponto de vista do estudante de graduação"]
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
        G2["G2: Avaliar a capacidade de interação do portal do discente do SIGAA/UnB, do ponto de vista do estudante de graduação"]
    end
    subgraph O["Nível operacional"]
        Q4["Q4: O estudante identifica onde está a função?"]
        Q5["Q5: Conclui as tarefas sem ajuda?"]
        Q6["Q6: A navegação evita esforço desnecessário?"]
        Q7["Q7: O sistema evita perda de trabalho após erros?"]
        Q8["Q8: As páginas podem ser usadas por pessoas com deficiência?"]
        Q9["Q9: Compreende as informações sem legenda?"]
        Q10["Q10: O estudante fica satisfeito?"]
    end
    subgraph Qt["Nível quantitativo"]
        M4["M4: Acerto na primeira escolha de menu"]
        M5["M5: Taxa de conclusão sem ajuda"]
        M6["M6: Tempo relativo de execução"]
        M7["M7: Desvio de caminho"]
        M8["M8: Taxa de recuperação de erros"]
        M9["M9: Erros automáticos de acessibilidade por página"]
        M10["M10: Critérios manuais de acessibilidade atendidos"]
        M11["M11: Interpretação correta sem legenda"]
        M12["M12: Pontuação SUS"]
    end
    G2 --> Q4 & Q5 & Q6 & Q7 & Q8 & Q9 & Q10
    Q4 --> M4
    Q5 --> M5
    Q6 --> M6 & M7
    Q7 --> M8
    Q8 --> M9 & M10
    Q9 --> M11
    Q10 --> M12
```

*Figura 3 - Hierarquia GQM do objetivo G2 - Capacidade de Interação. Fonte: gerado pelo Claude e revisado por Felipe Campêlo (2026).*

## G3 - Flexibilidade (Portabilidade)

```mermaid
flowchart TD
    subgraph C["Nível conceitual"]
        G3["G3: Avaliar a flexibilidade do portal do discente do SIGAA/UnB, do ponto de vista do estudante de graduação"]
    end
    subgraph O["Nível operacional"]
        Q11["Q11: As tarefas funcionam nos navegadores mais usados?"]
        Q12["Q12: O SIGAA se adapta a celular, tablet e toque?"]
    end
    subgraph Qt["Nível quantitativo"]
        M13["M13: Compatibilidade entre navegadores"]
        M14["M14: Páginas adaptadas a telas pequenas e ao toque"]
        M15["M15: Tempo relativo no celular"]
    end
    G3 --> Q11 & Q12
    Q11 --> M13
    Q12 --> M14 & M15
```

*Figura 4 - Hierarquia GQM do objetivo G3 - Flexibilidade. Fonte: gerado pelo Claude e revisado por Felipe Campêlo (2026).*

## G4 - Eficiência de Desempenho

```mermaid
flowchart TD
    subgraph C["Nível conceitual"]
        G4["G4: Avaliar a eficiência de desempenho das páginas do portal do discente do SIGAA/UnB, do ponto de vista do estudante de graduação"]
    end
    subgraph O["Nível operacional"]
        Q13["Q13: As páginas carregam em tempo aceitável?"]
        Q14["Q14: O uso de recursos é compatível com rede móvel?"]
    end
    subgraph Qt["Nível quantitativo"]
        M16["M16: Tempo de carregamento em rede comum"]
        M17["M17: Tempo de carregamento em rede móvel simulada"]
        M18["M18: Peso transferido por página"]
        M19["M19: Requisições por página"]
    end
    G4 --> Q13 & Q14
    Q13 --> M16 & M17
    Q14 --> M18 & M19
```

*Figura 5 - Hierarquia GQM do objetivo G4 - Eficiência de Desempenho. Fonte: gerado pelo Claude e revisado por Felipe Campêlo (2026).*

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 17/10/2026 | Diagramas GQM geral e por objetivo | Felipe Campêlo |
| 1.2 | 18/10/2026 | Numeração e legendas das figuras; nomes das métricas; níveis GQM nas Figuras 2 a 4 | Felipe Campêlo |
| 2.0 | 18/10/2026 | Alinhamento à Fase 1 reestruturada: objetivo G4, questões Q1 a Q14, métricas M1 a M19 e legendas no padrão da Fase 1 | Felipe Campêlo |
