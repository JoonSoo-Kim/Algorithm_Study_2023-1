# 순차 검색 알고리즘
def sequentialSearch(keyList: list, targetNum: int) -> int:
    targetLocation = 0;

    while targetLocation <= len(keyList) - 1 and keyList[targetLocation] != targetNum:
        targetLocation += 1

    if targetLocation == len(keyList):
        return -1
    else:
        return targetLocation


numList = [3, 5, 2, 1, 7, 9]
loc = sequentialSearch(numList, 4)
print(loc)
loc = sequentialSearch(numList, 2)
print(loc)