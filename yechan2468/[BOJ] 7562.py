import sys

input = sys.stdin.readline
source = [0, 0, 0]  # x, y, depth
destination = [0, 0]


def get_possible_moves(visited: list[list[bool]], coordinate: tuple[int, int, int]) -> list[tuple[int, int]]:
    result = []
    x, y, depth = coordinate
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    for i in range(8):
        if 0 <= x + dx[i] < len(visited) and 0 <= y + dy[i] < len(visited) and \
           not visited[x + dx[i]][y + dy[i]]:
            result.append((x + dx[i], y + dy[i], depth+1))
    return result


def dfs(visited: list[list[bool]], source: tuple[int, int, int], destination: tuple[int, int]):
    stack = [source]
    while stack:
        x, y, depth = stack.pop(0)
        if (x, y) == destination:
            return depth
        if not visited[x][y]:
            visited[x][y] = True
            stack.extend(get_possible_moves(visited, (x, y, depth)))


def solve(board_size: int) -> None:
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    source = tuple(list(map(int, input().split())) + [0])
    destination = tuple(map(int, input().split()))

    print(dfs(visited, source, destination))


for _ in range(testcase_count := int(input())):
    solve(board_size := int(input()))
