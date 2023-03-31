from math import inf
from itertools import combinations
import sys

n = int(sys.stdin.readline())
s = []
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

stats = dict()
for i in combinations(range(n), 2):
    if i[0] < i[1]:
        stats[i] = s[i[0]][i[1]] + s[i[1]][i[0]]

def get(key: tuple) -> int:
    result = 0
    for i in combinations(key, 2):
        result += stats[i]
    return result

result = inf
for i in combinations(range(n), n//2):
    i = tuple(sorted(list(i)))
    j = tuple(sorted(list(set(range(n)) - set(i))))
    result = min(abs(get(i) - get(j)), result)

print(int(result))