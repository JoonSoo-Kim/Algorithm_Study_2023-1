import sys

input = sys.stdin.readline
n, max_weight = map(int, input().split())
bag = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
prev, curr = [0] * (max_weight+1), []

for i in range(1, n+1):
    weight, value = bag[i]
    curr = prev[:]
    if weight <= max_weight:
        curr[weight] = max(curr[weight], value)
    for j in range(1, max_weight-weight+1):
        curr[weight+j] = max(curr[weight+j], prev[j] + value)
    prev = curr[:]
    print(curr)


print(max(curr))
