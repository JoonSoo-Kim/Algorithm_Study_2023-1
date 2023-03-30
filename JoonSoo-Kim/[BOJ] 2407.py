import sys
input = sys.stdin.readline

def combination(leftNumber: int, rightNumber: int) -> int:
    numerator = leftNumber
    denominator = rightNumber

    for number in range(1, rightNumber):
        numerator *= (leftNumber - number)
        denominator *= number

    return numerator // denominator


n, m = map(int, input().split())
print(combination(n, m))