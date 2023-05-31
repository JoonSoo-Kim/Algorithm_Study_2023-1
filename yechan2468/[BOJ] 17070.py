# import sys
# from enum import Enum
#
#
# class State(Enum):
#     HORIZONTAL = 0
#     VERTICAL = 1
#     DIAGONAL = 2
#
#
# def collided(x, y, state, obstacles):
#     if x >= len(obstacles) or y >= len(obstacles):
#         return True
#     if obstacles[y][x]:
#         return True
#     match state:
#         case State.HORIZONTAL:
#             if obstacles[y][x-1]:
#                 return True
#         case State.VERTICAL:
#             if obstacles[y-1][x]:
#                 return True
#         case State.DIAGONAL:
#             if obstacles[y][x-1] or obstacles[y-1][x] or obstacles[y-1][x-1]:
#                 return True
#     return False
#
#
# def arrived(x, y, n):
#     global answer
#     answer += 1 if (x == n-1 and y == n-1) else 0
#
#
# def solve(x, y, state, obstacles):
#     if collided(x, y, state, obstacles) or arrived(x, y, len(obstacles)):
#         return
#     match state:
#         case State.HORIZONTAL:
#             solve(x+1, y, state.HORIZONTAL, obstacles)
#             solve(x+1, y+1, state.DIAGONAL, obstacles)
#         case State.VERTICAL:
#             solve(x, y+1, state.VERTICAL, obstacles)
#             solve(x+1, y+1, state.DIAGONAL, obstacles)
#         case State.DIAGONAL:
#             solve(x+1, y, state.HORIZONTAL, obstacles)
#             solve(x, y+1, state.VERTICAL, obstacles)
#             solve(x+1, y+1, state.DIAGONAL, obstacles)
#
#
# sys.setrecursionlimit(1_000_001)
# n = int(sys.stdin.readline())
# obstacles = [list(map(lambda x: bool(int(x)), sys.stdin.readline().split())) for _ in range(n)]
# answer = 0
#
# solve(1, 0, State.HORIZONTAL, obstacles)
#
# print(answer)

# https://www.acmicpc.net/board/view/44217


import sys
from enum import IntEnum


class State(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL = 2


n = int(sys.stdin.readline())
obstacles = [list(map(lambda x: bool(int(x)), sys.stdin.readline().split())) for _ in range(n)]
memo = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
memo[0][1][State.HORIZONTAL] = 1

for i in range(n):
    for j in range(1, n):
        if obstacles[i][j]:
            continue
        memo[i][j][State.HORIZONTAL] += memo[i][j-1][State.HORIZONTAL] + memo[i][j-1][State.DIAGONAL]
        if i == 0:
            continue
        memo[i][j][State.VERTICAL] += memo[i-1][j][State.VERTICAL] + memo[i-1][j][State.DIAGONAL]
        if not obstacles[i-1][j] and not obstacles[i][j-1]:
            memo[i][j][State.DIAGONAL] += sum(memo[i-1][j-1])

print(sum(memo[n-1][n-1]))
