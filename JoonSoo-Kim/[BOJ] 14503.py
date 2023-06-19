import sys
input = sys.stdin.readline

class Cleaner:
    def __init__(self, n: int, m: int, room: list, r: int, c: int, d: int):
        self.n = n
        self.m = m
        self.room = room
        self.x = r
        self.y = c
        self.direction = d
        self.cnt = 0

    def is_dirty(self, x, y) -> bool:
        return not self.room[x][y]

    def clean(self):
        self.room[self.x][self.y] = 2

    def check_four_sides(self) -> bool:
        # 주변 4칸 중 청소되지 않은 빈 칸 찾기
        tmp1 = self.is_dirty(self.x+1, self.y) \
               or self.is_dirty(self.x, self.y+1)
        tmp2 = self.is_dirty(self.x-1, self.y) \
               or self.is_dirty(self.x, self.y-1)
        return tmp1 or tmp2

    def check_forward(self) -> bool:
        if self.direction == 0:
            return self.room[self.x-1][self.y] == 0
        if self.direction == 1:
            return self.room[self.x][self.y+1] == 0
        if self.direction == 2:
            return self.room[self.x+1][self.y] == 0
        if self.direction == 3:
            return self.room[self.x][self.y-1] == 0

    def check_backward(self) -> bool:

        if self.direction == 0:
            return self.room[self.x+1][self.y] != 1
        if self.direction == 1:
            return self.room[self.x][self.y-1] != 1
        if self.direction == 2:
            return self.room[self.x-1][self.y] != 1
        if self.direction == 3:
            return self.room[self.x][self.y+1] != 1

    def move_forward(self):
        if self.direction == 0:
            self.x -= 1
        if self.direction == 1:
            self.y += 1
        if self.direction == 2:
            self.x += 1
        if self.direction == 3:
            self.y -= 1

    def move_backward(self):
        if self.direction == 0:
            self.x += 1
        if self.direction == 1:
            self.y -= 1
        if self.direction == 2:
            self.x -= 1
        if self.direction == 3:
            self.y += 1

    def spin(self):
        self.direction = (self.direction + 3) % 4
    def get_cnt(self) -> int:
        return self.cnt

    def operate(self) -> bool:
        if self.is_dirty(self.x, self.y):
            self.clean()
            print(self.x, self.y)
            self.cnt += 1

        if self.check_four_sides():
            self.spin()
            if self.check_forward():
                self.move_forward()
        else:
            if self.check_backward():
                self.move_backward()
            else:
                return False
        return True

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [[0] * m for _ in range(n)]
for i in range(n):
    room[i] = list(map(int, input().split()))

cleaner = Cleaner(n, m, room, r, c, d)
while True:
    if not cleaner.operate():
        break
print(cleaner.get_cnt())
