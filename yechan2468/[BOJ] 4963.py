from collections import deque
import sys

def get_adjacent(row, col, h, w):
    return filter(
        lambda x: not (x[0] == row and x[1] == col) and (0 <= x[0] < h and 0 <= x[1] < w),
        ((y, x) for y in range(row-1, row+2) for x in range(col-1, col+2))
    )

def bfs(visited, row, col):
    queue = deque([(row, col)])
    visited[row][col] = True
    while queue:
        row, col = queue.popleft()
        for row, col in get_adjacent(row, col, len(visited), len(visited[0])):
            if not visited[row][col]:
                visited[row][col] = True
                queue.append((row, col))
    return 1

while True:
    result = 0
    w, h = map(int, sys.stdin.readline().split())
    if h == 0:
        break

    visited = []
    for _ in range(h):
        visited.append(list(map(lambda x: not int(x), sys.stdin.readline().split())))

    for row in range(h):
        for col in range(w):
            if not visited[row][col]:
                result += bfs(visited, row, col)
    
    print(result)
