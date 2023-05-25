# boj 14497
# 주난의 난
from collections import deque
import sys

# n: 행의 개수, m: 열의 개수
n, m = map(int, sys.stdin.readline().split())
y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
# 인덱스에 맞게 좌표값들에 -1
y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1

a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
level = [[-1] * m for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


q = deque()
# 주난의 위치를 큐에 삽입
q.append((y1, x1))
level[y1][x1] = 0

cnt = 0
while a[y2][x2] != '0': # 범인을 찾을 때까지 반복
    cnt += 1
    temp = deque()
    # level 별로 bfs 적용
    while q: # q에 원소가 없을 때까지 반복
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or level[ny][nx] != -1:
                continue
            level[ny][nx] = cnt
            if a[ny][nx] != '0': # (ny, nx)에 해당하는 값이 0이라면
                a[ny][nx] = '0' # 0으로 업데이트
                temp.append((ny, nx)) # 해당 위치를 temp 큐에 삽입
            else: # 만약 (ny, nx)에 해당하는 값이 0이라면
                q.append((ny, nx)) 
    q = temp # q를 temp로 업데이트하여 다음 level 탐색

print(level[y2][x2])
