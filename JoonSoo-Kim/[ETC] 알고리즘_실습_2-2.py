# 배열의 수 더하기
def sumVersionOne(numList: list) -> int:
    result = 0

    for num in numList:
        result += num

    return result

def sumVersionTwo(numList: list) -> int:
    result = 0

    for index in range(len(numList)):
        result += numList[index]

    return result

numList = [3, 5, 2, 1, 7, 9]
# sum1 결과
print(sumVersionOne(numList))
# sum2 결과
print(sumVersionTwo(numList))
