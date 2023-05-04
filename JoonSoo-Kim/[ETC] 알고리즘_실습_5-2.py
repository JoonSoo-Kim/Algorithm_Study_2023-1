# 플로이드 알고리즘 구현
def print_floyd(graph: list, n: int):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][j]+graph[k][j])

    path = [[0 for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    path[i][j] = k + 1
                    graph[i][j] = graph[i][k] + graph[k][j]

    print_matrix(graph)
    print()
    print_matrix(path)

def print_matrix(matrix: list):
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()


inf = 1000
g = [[0, 1, inf, 1, 5],
     [9, 0, 3, 2, inf],
     [inf, inf, 0, 4, inf],
     [inf, inf, 2, 0, 3],
     [3, inf, inf, inf, 0]]

print_matrix(g)
print()
print_floyd(g, 5)