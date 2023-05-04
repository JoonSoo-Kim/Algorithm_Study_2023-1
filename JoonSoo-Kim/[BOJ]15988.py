import sys
input = sys.stdin.readline

sum_list = [0, 1, 2, 4]
t = int(input())

for i in range(4, 1000001):
    sum = sum_list[i - 1] + sum_list[i - 2] + sum_list[i - 3]
    sum_list.append(sum%1000000009)

for _ in range(t):
    n = int(input())
    print(sum_list[n] % 1000000009)
