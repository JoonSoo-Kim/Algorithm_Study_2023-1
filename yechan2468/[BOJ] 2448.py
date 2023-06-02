import math
import sys


# n = 3 = 3*(2**0)
# k = 0
#   *
#  * *
# *****

# n = 6 = 3*(2**1)
# k = 1
#      *
#     * *
#    *****
#   *     *
#  * *   * *
# ***** *****

# n = 12 = 3*(2**2)
# k = 2
#            *
#           * *
#          *****
#         *     *
#        * *   * *
#       ***** *****
#      *           *
#     * *         * *
#    *****       *****
#   *     *     *     *
#  * *   * *   * *   * *
# ***** ***** ***** *****


def draw_triangle(arr, pos):
    x, y = pos
    arr[y][x+2] = '*'
    arr[y+1][x+1] = arr[y+1][x+3] = '*'
    arr[y+2][x] = arr[y+2][x+1] = arr[y+2][x+2] = arr[y+2][x+3] = arr[y+2][x+4] = '*'


def solve(arr, n, k, pos=(0, 0)):
    if n == 3:
        draw_triangle(arr, pos)
        return
    x, y = pos
    pos_up = (x + 3 * 2**(k-1), y)
    pos_left = (x, y + n//2)
    pos_right = (x + n, y + n//2)

    solve(arr, n//2, k-1, pos_up)
    solve(arr, n//2, k-1, pos_left)
    solve(arr, n//2, k-1, pos_right)


def print_answer(arr):
    for line in arr:
        for char in line:
            sys.stdout.write(char)
        sys.stdout.write('\n')
    sys.stdout.flush()


n = int(sys.stdin.readline())
k = int(math.log2(n/3))
arr = [[' ' for _ in range(6*(2**k))] for _ in range(n)]

solve(arr, n, k)
print_answer(arr)
