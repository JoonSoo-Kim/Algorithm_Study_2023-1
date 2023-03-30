import sys

n, m = map(int, sys.stdin.readline().split())
queue = [i for i in range(1, n+1)]
prev, curr, result = 0, 0, 0

for target in (targets := map(int, sys.stdin.readline().split())):
    curr = queue.index(target)
    result += min(abs(curr - prev), abs(len(queue) - abs(curr - prev)))
    queue.pop(curr)
    prev = curr

print(result)
