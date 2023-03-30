import sys
input = sys.stdin.readline

def findPrimeNumber(number: int) ->int:
    maxNumber = number * 2
    numberList= [False, False] + [True] * (maxNumber - 1)
    primeList = []

    for index in range(2, maxNumber+1):
        if numberList[index]:
            if index > number:
                primeList.append(index)
            for indexTwo in range(2*index, maxNumber+1,index):
                numberList[indexTwo] = False

    return len(primeList)

nNumber = 0

while True:
    nNumber = int(input())
    if nNumber == 0:
        break
    print(findPrimeNumber(nNumber))