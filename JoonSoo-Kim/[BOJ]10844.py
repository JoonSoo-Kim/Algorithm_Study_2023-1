import sys
input = sys.stdin.readline

n = int(input())
current = [1] * 10


for loop in range(n-1):
    prev = current[:]
    for i in range(1, 9):
        current[i] = prev[i-1] + prev[i+1]
    current[0] = prev[1]
    current[9] = prev[8]
    if loop == 0:
        current[1] = prev[2] + 1

current[0] = 0
print(sum(current) % 1000000000)
