# Demonstração do Algoritmo de Floyd-Warshall

Este repositório contém uma implementação educacional do algoritmo de **Floyd-Warshall** em Python, voltado para demonstração em sala de aula.

O algoritmo é utilizado para encontrar o **menor caminho entre todos os pares de vértices** em um grafo ponderado, podendo lidar com pesos positivos e detectar conexões indiretas eficientes por meio de vértices intermediários.

## Matriz de Adjacência Inicial

```
      A   B   C   D
    ----------------
A |   0   3 INF   7
B |   8   0   2 INF
C |   5 INF   0   1
D |   2 INF INF   0
```

## O que o código faz

1. Inicializa a matriz de distâncias com os valores fornecidos.
2. Para cada vértice `k`, tenta usá-lo como intermediário entre todos os pares `(i, j)`.
3. Atualiza `dist[i][j]` se `dist[i][k] + dist[k][j] < dist[i][j]`.
4. Imprime a matriz após cada iteração, com cabeçalho alinhado (A, B, C, D).

## Saída esperada

O programa imprime a matriz inicial e, em seguida, a matriz atualizada após cada iteração do vértice intermediário (`k = A`, `k = B`, etc.).
Ao final, a matriz representa os menores caminhos entre todos os pares.

## Como executar

```bash
python floyd_warshall.py
```

> Certifique-se de que está utilizando Python 3.

---

Desenvolvido para fins educacionais por Rodrigo e adaptado para uso demonstrativo em disciplinas de Grafos e Análise de Algoritmos.