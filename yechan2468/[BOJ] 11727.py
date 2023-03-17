import sys

n = int(sys.stdin.readline())
memo = [1, 3, 0]
for i in range(n-2):
    memo[(i+2)%3] = (memo[i%3] * 2 + memo[(i+1)%3]) % 10_007

print(memo[n%3-1])
