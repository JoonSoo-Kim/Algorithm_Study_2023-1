import sys
input = sys.stdin.readline


def w(a: int, b: int, c: int) -> int:
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if num_list[a][b][c]:
        return num_list[a][b][c]

    if a < b and b < c:
        num_list[a][b][c] = \
            w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1, c)
        return num_list[a][b][c]

    num_list[a][b][c] = \
        w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return num_list[a][b][c]

num_list = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')


