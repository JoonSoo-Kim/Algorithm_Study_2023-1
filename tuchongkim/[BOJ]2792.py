# boj 2792
# 보석 상자
import sys

n, m = map(int, sys.stdin.readline().split())

jewls =[] # 보석 종류별 개수를 저장
for _ in range(m):
    jewls.append(int(sys.stdin.readline().rstrip()))
jewls.sort()

# 개수가 많은 보석을 계속 나눠서 질투심을 만족하는지 확인
low = 1
high = jewls[-1]
result = 1000000000 # 질투심

def check(mid):
    num = 0 # 몇 명에게 분배할 것인가
    for i in range(m):
        if jewls[i] > mid:
            num += jewls[i] // mid
            if jewls[i] % mid:
                num += 1
        else:
            num += 1
    return n >= num

while low <= high: # (1, 7) -> (1, 3) -> (2, 3) -> (3, 3)
    mid = (low + high) // 2 # 4 -> 2 -> 2 -> 3 
    if check(mid):
        result = min(result, mid)
        high = mid - 1
    else:
        low = mid + 1

print(result)