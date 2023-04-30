# boj 1931

import sys

n = int(sys.stdin.readline())
v = [] 

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    v.append((end, start))
v.sort()

start = v[0][1] # 첫번째 시작 시간
end = v[0][0] # 첫번째 종료 시간
result = 1 # 회의 개수
for i in range(1, n):
    if v[i][1] < end: # 시간이 겹칠 때
        continue
    start = v[i][1]
    end = v[i][0]
    result += 1
    
print(result)
