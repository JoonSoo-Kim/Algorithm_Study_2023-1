
n, k = map(int, input().split())
num_list = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
i = 1
target = -10000000
for number in num_list:
    prefix_sum[i] = prefix_sum[i-1] + number
    i += 1
for j in range(k, n+1):
    temp = prefix_sum[j] - prefix_sum[j - k]
    target = max(target, temp)
print(target)