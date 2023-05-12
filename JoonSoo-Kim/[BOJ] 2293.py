import sys
input = sys.stdin.readline

n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
num_list = [0 for _ in range(k+1)]

num_list[0] = 1

for coin in c:
    for i in range(coin, k+1):
        if i - coin >= 0:
            num_list[i] += num_list[i-coin]

print(num_list[k])