# 이진 탐색
def binarySearch(numList: list, targetNumber):
    lowIndex, highIndex = 0, len(numList) - 1
    resultIndex = 0

    while lowIndex <= highIndex and resultIndex == 0:
        midIndex = (lowIndex + highIndex) // 2

        if targetNumber == numList[midIndex]:
            resultIndex = midIndex
        elif targetNumber < numList[midIndex]:
            highIndex = midIndex - 1
        else:
            lowIndex = midIndex + 1

    return resultIndex


numList = [1, 3, 5, 6, 7, 9, 10, 14, 17, 19]
print(binarySearch(numList, 17))