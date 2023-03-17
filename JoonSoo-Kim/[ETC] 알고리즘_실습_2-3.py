# 교환 정렬
def exchangeSort(numList: list) -> list:
    for firstIndex in range(len(numList)):
        for secondIndex in range(firstIndex, len(numList)):
            if numList[firstIndex] > numList[secondIndex]:
                numList[firstIndex], numList[secondIndex] = numList[secondIndex], numList[firstIndex]

    return numList


numList = [3, 2, 5, 7, 1, 9, 4, 6, 8]
print(exchangeSort(numList))