import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline().rstrip())
a = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
h = max(map(max, a))
visited = [[0] * n for _ in range(n)]

def dfs(y, x, k):
    visited[y][x] = 1
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            continue
        if not visited[ny][nx] and a[ny][nx] > k:
            dfs(ny, nx, k)

result = 1
for k in range(1, h+1):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[j][i] > k and not visited[j][i]:
                dfs(j, i, k)
                cnt += 1
    result = max(result, cnt)

print(result)
