import sys
input = sys.stdin.readline

maxNum = 1000000
fxList = [1] * 1000001
gxList = [0] * 1000001

def getAllGx():
    for divisor in range(2, maxNum + 1):
        for multipleIndex in range(divisor, maxNum + 1, divisor):
            fxList[multipleIndex] += divisor

    for divisorIndex in range(1, maxNum + 1):
        gxList[divisorIndex] = gxList[divisorIndex - 1] + fxList[divisorIndex]


getAllGx()

testCaseNum = int(input())

for _ in range(testCaseNum):
    nNum = int(input())
    print(gxList[nNum])