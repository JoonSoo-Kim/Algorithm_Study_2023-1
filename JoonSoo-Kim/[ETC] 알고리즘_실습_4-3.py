# 큰 정수곱셈
import math

def largeIntegerProduct(firstNum: int, secondNum: int) -> int:
    threshold = 1
    maxDigit = max(getDigit(firstNum), getDigit(secondNum))

    if firstNum == 0 or secondNum == 0:
        return 0
    elif maxDigit <= threshold:
        return firstNum * secondNum
    else:
        mNum = int(maxDigit/2)
        xNum = firstNum // pow(10, mNum)
        yNum = firstNum % pow(10, mNum)
        wNum = secondNum // pow(10, mNum)
        zNum = secondNum % pow(10, mNum)
        rNum = largeIntegerProduct(xNum+yNum, wNum+zNum)
        pNum = largeIntegerProduct(xNum, wNum)
        qNum = largeIntegerProduct(yNum, zNum)

        return pNum * pow(10, 2*mNum) + (rNum - pNum - qNum) * pow(10, mNum) + qNum

def getDigit(num: int):
    length = 0

    while num < 0:
        num //= 10
        length += 1

    return length

a = 1234567812345678
b = 2345678923456789

print(largeIntegerProduct(a, b))
print(a*b)