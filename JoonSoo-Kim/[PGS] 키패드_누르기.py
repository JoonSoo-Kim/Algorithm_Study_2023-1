class Hand:
    def __init__(self, main_handed: bool):
        self.col = -1
        self.row = -1
        self.num = -1
        self.main = main_handed


class Phone:
    def __init__(self, numbers: int, hand: str):
        self.numbers = numbers
        if hand == "left":
            self.left = Hand(1)
            self.right = Hand(0)
        if hand == "right":
            self.left = Hand(0)
            self.right = Hand(1)

    def move_left(self, num: int):
        self.left.num = num
        self.left.row = num // 3
        self.left.col = 0

    def move_right(self, num: int):
        self.right.num = num
        self.right.row = num // 4
        self.right.col = 2

    def move_middle(self, num: int, hand: Hand):
        hand.num = num
        hand.row = num // 3
        hand.col = 1

    def get_distance(self, num: int, hand: Hand) -> int:
        row = num // 3
        col = 1
        return abs(row - hand.row) + abs(col - hand.col)

    def operate(self) -> str:
        result = ""

        for num in self.numbers:
            if num % 3 == 1:
                result += "L"
                self.move_left(num)

            if num % 3 == 0:
                result += "R"
                self.move_right(num)

            if num % 3 == 2:
                if (self.get_distance(num, self.left) < self.get_distance(num,
                                                                          self.right)) \
                        or (
                        self.get_distance(num, self.left) == self.get_distance(
                    num, self.right)
                        and self.left.main == True):
                    result += "L"
                    self.move_middle(num, self.left)

                if (self.get_distance(num, self.left) < self.get_distance(num,
                                                                          self.right)) \
                        or (
                        self.get_distance(num, self.left) == self.get_distance(
                    num, self.right)
                        and self.right.main == True):
                    result += "R"
                    self.move_middle(num, self.right)


def solution(numbers, hand):
    phone = Phone(numbers, hand)
    answer = phone.operate()
    return answer