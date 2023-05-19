# 2529
# 부등호
import sys

n = int(sys.stdin.readline())
a = list(sys.stdin.readline().split())
used = [0] * 10 # 숫자를 사용하면 1, 사용 안했으면 0
result = []

def valid(x, y, op): # int, int, str
    if x < y and op == '<':
        return True
    if x > y and op == '>':
        return True
    return False

def check(idx, num_str): # int, str
    if idx == n + 1: # 종료조건
        result.append(num_str)
    else:
      for i in range(10):
          if used[i]:
              continue
          if idx == 0 or valid(int(num_str[idx - 1]), i, a[idx - 1]):
              used[i] = 1
              check(idx + 1, num_str + str(i))
              used[i] = 0

check(0, '')
result.sort()
print(result[-1])
print(result[0])
