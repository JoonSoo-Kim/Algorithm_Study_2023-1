# boj 1202

import sys
from queue import PriorityQueue

n, k = map(int, sys.stdin.readline().split())
v = []
bag = []

for i in range(n):
    mass, value = map(int, sys.stdin.readline().split())
    v.append((mass, value))

for i in range(k):
    bag.append(int(sys.stdin.readline()))

v.sort()
bag.sort()
pq = PriorityQueue()

j = 0
result = 0
for i in range(k):
    while j < n and v[j][0] <= bag[i]:
        pq.put(-v[j][1]) # python에서 우선순위 큐는 오름차순이기 때문에
        j += 1
    if pq.empty() == False:
        result -= pq.get()

print(result)
