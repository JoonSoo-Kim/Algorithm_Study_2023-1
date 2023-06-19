import sys
input = sys.stdin.readline

class Dice:
    top = 0
    bottom = 0
    up = 0
    down = 0
    left = 0
    right = 0

    def __init__(self, n, m, my_map, x, y, k):
        self.n = n
        self.m = m
        self.my_map = my_map
        self.x = x
        self.y = y
        self.k = k

    def move_position(self, x, y):
        self.x += x
        self.y += y
    def move_dice_east(self):
        tmp = self.bottom
        self.bottom = self.right
        self.right = self.top
        self.top = self.left
        self.left = tmp

    def move_dice_west(self):
        tmp = self.bottom
        self.bottom = self.left
        self.left = self.top
        self.top = self.right
        self.right = tmp

    def move_dice_north(self):
        tmp = self.bottom
        self.bottom = self.up
        self.up = self.top
        self.top = self.down
        self.down = tmp

    def move_dice_south(self):
        tmp = self.bottom
        self.bottom = self.down
        self.down = self.top
        self.top = self.up
        self.up = tmp


    def copy(self):
        if my_map[self.y][self.x] == 0:
            my_map[self.y][self.x] = self.bottom
        else:
            self.bottom = my_map[self.y][self.x]
            my_map[self.y][self.x] = 0

    def roll(self, command: int):
        # 원래 각 command에 따라 move 메서드를 하나 더 넣어야 좋은 메서드일듯
        if command == 1:
            if self.x == self.m - 1:
                return
            self.move_position(1, 0)
            self.move_dice_east()
            self.copy()

        if command == 2:
            if self.x == 0:
                return
            self.move_position(-1, 0)
            self.move_dice_west()
            self.copy()

        if command == 3:
            if self.y == 0:
                return
            self.move_position(0, -1)
            self.move_dice_north()
            self.copy()

        if command == 4:
            if self.y == self.n - 1:
                return
            self.move_position(0, 1)
            self.move_dice_south()
            self.copy()

        print(self.top)


n, m, y, x, k = map(int, input().split())
my_map = [[0] * m for _ in range(n)]
for i in range(n):
    my_map[i] = list(map(int, input().split()))
commands = list(map(int, input().split()))
dice = Dice(n, m, my_map, x, y, k)

for cmd in commands:
    dice.roll(cmd)