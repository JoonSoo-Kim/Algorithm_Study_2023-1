import sys
import math
input = sys.stdin.readline

gcdNum, lcmNum = map(int, input().split())
divideNum = lcmNum // gcdNum  # 값1 * 값2 = lcm / gcd
minNum = lcmNum
minList = []

# 값1과 값2는 결과값에서 최대공약수를 나눈 값이 된다.
for firstNumber in range(1, int(math.sqrt(divideNum)) + 1):
    # 값2 = lcm / gcd / 값1 이므로 값1을 for문으로 반복시키면서 값2를 찾는다.
    secondNumber = int(divideNum / firstNumber)

    # 값1과 값2가 divideNum의 약수여야 적절한 값이 된다.
    if divideNum % firstNumber == 0 and divideNum % secondNumber == 0:
        if math.gcd(firstNumber, secondNumber) == 1:
            if secondNumber - firstNumber < minNum:
                minNum = secondNumber - firstNumber
                minList = [firstNumber, secondNumber]

# 값1과 값2에 최대공약수를 곱해야 결과값을 얻을 수 있다.
print(minList[0] * gcdNum, minList[1] * gcdNum)


