import sys

n = int(sys.stdin.readline().rstrip())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def qTree(y, x, size):
    if size == 1:
        return a[y][x]
    b = a[y][x]
    result = ""
    for i in range(x, x + size):
        for j in range(y, y + size):
            if b != a[j][i]:
                result += '('
                result += qTree(y, x, size // 2)
                result += qTree(y, x + size // 2, size // 2)
                result += qTree(y + size // 2, x, size // 2)
                result += qTree(y + size // 2, x + size // 2, size // 2)
                result += ')'
                return result
    return a[y][x]

print(qTree(0, 0, n))
