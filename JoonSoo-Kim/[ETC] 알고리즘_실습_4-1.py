# 빠른정렬
def quickSort(numList: list, lowIndex: int, highIndex: int) -> list:
    pivotPoint = lowIndex

    if(highIndex > lowIndex):
        partition(numList, lowIndex, highIndex, pivotPoint)
        quickSort(numList, lowIndex, pivotPoint-1)
        quickSort(numList, pivotPoint+1, highIndex)
        return numList
def partition(numList: list, lowIndex: int, highIndex: int, pivotIndex: int) -> list:
    rightLowIndex = lowIndex
    pivot = numList[lowIndex]

    for index in range(lowIndex+1, highIndex+1):
        if numList[index] < pivot:
            rightLowIndex += 1
            numList[index], numList[rightLowIndex] \
                = numList[rightLowIndex], numList[index]

    pivotIndex = rightLowIndex
    numList[lowIndex], numList[pivotIndex] \
        = numList[pivotIndex], numList[lowIndex]

    return numList

s = [3, 5, 2, 9, 10, 14, 4, 8]
quickSort(s, 0, 7)
print(s)