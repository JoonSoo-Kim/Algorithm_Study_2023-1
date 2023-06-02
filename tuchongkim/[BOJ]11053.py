"""
틀린 풀이 : 
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = 0
max_num = 0
for num in numbers:
    if num > max_num:
        cnt += 1
        max_num = num
print(cnt)

다른 풀이(binary search) :
import sys, bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
"""
# boj 11053
# 가장 긴 증가하는 부분 순열
# 각 숫자마다 최대 count를 저장
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
count = [1] * n

for i in range(1, n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            count[i] = max(count[j] + 1, count[i])

print(max(count))
