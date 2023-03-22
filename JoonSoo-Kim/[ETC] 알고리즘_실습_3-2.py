# 합병정렬
def mergeSort(number: int, numberList) -> list:
    firstLength = number // 2
    secondLength = number - firstLength
    firstList = [0 for _ in range(firstLength)]
    secondList = [0 for _ in range(secondLength)]

    if number > 1:
        firstList[0:firstLength] = numberList[0:firstLength]
        secondList[0:secondLength] = numberList[firstLength:]
        firstList = mergeSort(firstLength, firstList)
        secondList = mergeSort(secondLength, secondList)
        numberList = merge(firstLength, secondLength, firstList, secondList, numberList)
        return numberList
    else:
        return numberList
def merge(firstLength: int, secondLength: int, firstList: list, secondList: list, numberList: list):
    firstIndex = 0
    secondIndex = 0
    thirdIndex = 0

    while firstIndex < firstLength and secondIndex < secondLength:
        if firstList[firstIndex] < secondList[secondIndex]:
            numberList[thirdIndex] = firstList[firstIndex]
            firstIndex += 1
        else:
            numberList[thirdIndex] = secondList[secondIndex]
            secondIndex += 1
        thirdIndex += 1

    if firstIndex >= firstLength:
        numberList[thirdIndex:] = secondList[secondIndex:]
    elif secondIndex >= secondLength:
        numberList[thirdIndex:] = firstList[firstIndex:]
    return numberList

numberList = [27, 10, 12, 20, 25, 13, 15, 22]
numberList = mergeSort(8, numberList)
print(numberList)