# 12851
# 숨바꼭질2
from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
MAX = 200000
visited = [0] * (MAX+4)
ways = [0] * (MAX+4)

if n > k:
    ways[k] = 1
    while(n > k):
        n -= 1
        visited[k] += 1
if n == k:
    ways[k] = 1
else:
    visited[n] = 1
    ways[n] = 1
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        for next in (now-1, now+1, now*2):
            if 0 <= next <= MAX:
                if not visited[next]:
                    q.append(next)
                    visited[next] = visited[now] + 1
                    ways[next] += ways[now]
                elif visited[next] == visited[now] + 1:
                    ways[next] += ways[now]
    visited[k] -= 1

print(visited[k])
print(ways[k])