import collections


def getJewelNum(jewels: str, stones: str) -> int:
    frequency = collections.defaultdict(int)
    count = 0

    for fragment in stones:
        frequency[fragment] += 1

    for jewel in jewels:
        count += frequency[jewel]

    return count


jewels = input()
stone = input()
print(getJewelNum(jewels, stone))