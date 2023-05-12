from collections import deque
import sys


class Snake:
    time_elapsed = 0
    x = 0
    y = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    body = deque([(0, 0)])
    board = None

    def move_to(self, next_move):
        time, rotate_dir = next_move
        for _ in range(time - self.time_elapsed):
            self.forward()

            if self.collided() or not self.board.is_inside(self.x, self.y):
                print(self.time_elapsed)
                exit()

            self.stretch()
            if not self.eat_apple():
                self.shrink()

        self.rotate(rotate_dir)

    def forward(self):
        self.x += self.dx[self.dir]
        self.y += self.dy[self.dir]
        self.time_elapsed += 1

    def collided(self):
        return (self.x, self.y) in self.body

    def stretch(self):
        self.body.append(tuple([self.x, self.y]))

    def eat_apple(self):
        if self.board.apple_exist[self.x][self.y]:
            self.board.apple_exist[self.x][self.y] = False
            return True
        else:
            return False

    def shrink(self):
        self.body.popleft()

    def rotate(self, rotate_dir):
        match rotate_dir:
            case 'D':
                self.dir = (self.dir + 1) % 4
            case 'L':
                self.dir = (self.dir + 3) % 4


class Board:
    def __init__(self, board_size, apples):
        self.size = board_size
        self.apple_exist = [([False] * board_size) for _ in range(board_size)]
        for apple in apples:
            x, y = apple
            self.apple_exist[x][y] = True

    def is_inside(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size


input = sys.stdin.readline
board_size = int(input())
num_apple = int(input())

apples = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(num_apple)]

num_move = int(input())
moves = []
for _ in range(num_move):
    time, rotation_dir = input().split()
    moves.append(tuple([int(time), rotation_dir]))
moves.append(tuple([10101, 'D']))
moves.reverse()

snake = Snake()
snake.board = Board(board_size, apples)

while moves:
    snake.move_to(moves.pop())
print(snake.time_elapsed)
