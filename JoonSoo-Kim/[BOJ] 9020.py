import sys
input = sys.stdin.readline

# 시간이 부족하니까 각 테스트 케이스에 대해 소수를 구하는게 아니라 미리 소수를 구해두고 계산

def getPrimeNumbers(number: int) -> list:
    primeList = [False, False] + [True] * (number - 1)

    for firstIndex in range(2, number + 1):
        if primeList[firstIndex]:
            for secondIndex in range(2 * firstIndex, number + 1, firstIndex):
                primeList[secondIndex] = False

    return primeList

def printGoldbach(number: int, primeList: list) -> list:
    leftIndex = number // 2
    rightIndex = leftIndex

    for _ in range(10000):
        if primeList[leftIndex] and primeList[rightIndex]:
            print(leftIndex, rightIndex)
            break;
        leftIndex -= 1
        rightIndex += 1


repeatNumber = int(input())
for _ in range(repeatNumber):
    tNumber = int(input())
    primeList = getPrimeNumbers(10000)
    printGoldbach(tNumber, primeList)