#피보나치 수

import time

def getFibonacciByRecursion(number: int) -> int:
    if number <= 1:
        return number
    else:
        return getFibonacciByRecursion(number - 1) + getFibonacciByRecursion(number - 2)

def getFibonacciByIteration(number: int) -> int:
    if(number < 2):
        return number

    numList = [0 for _ in range(number + 1)]
    numList[0], numList[1] = 0, 1

    for index in range(2, number + 1):
        numList[index] = numList[index - 1] + numList[index - 2]

    return numList[number]

startTime = time.time()
for number in range(40):
    print(number, getFibonacciByRecursion(number))
endTime = time.time()
print(endTime - startTime, "\n")

startTime = time.time()
for number in range(40):
    print(number, getFibonacciByIteration(number))
endTime = time.time()
print(endTime - startTime)