import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if a[ny][nx] == 1 and not visited[ny][nx]:
            dfs(ny, nx)

t = int(input().strip())

for _ in range(t):
    m, n, k = map(int, input().split())
    a = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        a[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                result += 1
    print(result)