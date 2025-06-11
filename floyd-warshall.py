V = 4
INF = float('inf')

def floydWarshall(graph):
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    print(">>> MATRIZ INICIAL")
    printMatrix(dist)

    for k in range(V):
        print(f"\n>>> Iteração k = {chr(ord('A') + k)} ({k})")
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        printMatrix(dist)

def printMatrix(matrix):
    # Cabeçalho alinhado com largura fixa de 4 colunas
    header = "    " + "".join(f"{chr(ord('A') + j):>4}" for j in range(V))
    print(header)
    print("    " + "-" * (4 * V))

    for i in range(V):
        row = f"{chr(ord('A') + i)} |"
        for j in range(V):
            val = matrix[i][j]
            text = "INF" if val == INF else str(val)
            row += f"{text:>4}"
        print(row)

if __name__ == "__main__":
    graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]
    floydWarshall(graph)
