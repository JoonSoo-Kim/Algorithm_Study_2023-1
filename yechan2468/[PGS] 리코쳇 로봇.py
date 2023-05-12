from collections import deque


def move_up(x, y, board, move_count):
    while y > 0 and board[y - 1][x] != 'D':
        y -= 1
    return x, y, move_count

def move_down(x, y, board, move_count):
    while y < len(board) - 1 and board[y + 1][x] != 'D':
        y += 1
    return x, y, move_count

def move_left(x, y, board, move_count):
    while x > 0 and board[y][x - 1] != 'D':
        x -= 1
    return x, y, move_count

def move_right(x, y, board, move_count):
    while x < len(board[0]) - 1 and board[y][x + 1] != 'D':
        x += 1
    return x, y, move_count


def bfs(src, dest, board, visited):
    move_count = 0
    queue = deque([(src[0], src[1], move_count)])
    while queue:
        x, y, move_count = queue.popleft()
        if x == dest[0] and y == dest[1]:
            return move_count
        if not visited[y][x]:
            visited[y][x] = True
            queue.extend([tuple(move_up(x, y, board, move_count + 1)),
                          tuple(move_down(x, y, board, move_count + 1)),
                          tuple(move_left(x, y, board, move_count + 1)),
                          tuple(move_right(x, y, board, move_count + 1))])
    return -1


def solution(board):
    src = [0, 0]  # x, y
    dest = [0, 0]
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 'D':
                visited[y][x] = True
            elif board[y][x] == 'R':
                src = x, y
            elif board[y][x] == 'G':
                dest = x, y
    return bfs(src, dest, board, visited)
