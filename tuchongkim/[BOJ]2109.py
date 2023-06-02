# boj 2109
# 순회강연
import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
v = []

for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    v.append((d, p))
v.sort() # d를 기준으로 오름차순 정렬

pq = PriorityQueue()
result = 0
for i in range(n):
    pq.put(v[i][1]) # p값을 우선순위큐에 삽입
    if pq.qsize() > v[i][0]: # d값에 따라 현재 가질 수 있는 최대값들만 남겨놓음
        pq.get()
while not pq.empty():
    result += pq.get()

print(result)

