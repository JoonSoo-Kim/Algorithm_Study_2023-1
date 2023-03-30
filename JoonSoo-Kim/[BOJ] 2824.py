import sys
input = sys.stdin.readline

def getGCD(firstNumber: int, secondNumber: int) -> int:
    while secondNumber > 0:
        firstNumber, secondNumber = secondNumber, firstNumber % secondNumber
    return firstNumber


n = int(input())
nNumber = 1
nNumberList = list(map(int, input().split()))
for nNumberElement in nNumberList:
    nNumber *= nNumberElement

m = int(input())
mNumber = 1
mNumberList = list(map(int, input().split()))
for mNumberElement in mNumberList:
    mNumber *= mNumberElement

resultNumber = getGCD(nNumber, mNumber)
if resultNumber // 1000000000 > 0:
    resultNumber = str(resultNumber)[-9:]

print(resultNumber)