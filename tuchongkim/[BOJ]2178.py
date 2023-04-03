import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# 깊이와 방문여부 동시에 표현
visited = [[0] * m for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque([(0, 0)]) # 시작위치
visited[0][0] = 1

# 큐가 완전히 빌 때까지 반복
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m or maze[ny][nx] == 0:
            continue
        if visited[ny][nx]:
            continue
        visited[ny][nx] = visited[y][x] + 1
        q.append((ny, nx))

print(visited[n - 1][m - 1])