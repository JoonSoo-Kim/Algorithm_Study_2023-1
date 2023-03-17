import sys

def makeProperParenthesis(listString: str) -> int:
    numbersList = listString.replace('+', '-').split('-')
    operatorsList = []
    resultNumber = 0
    currentNumber = 0
    index = 0

    for numbersIndex in range(len(numbersList)):
        numbersList[numbersIndex] = int(numbersList[numbersIndex])

    for char in listString:
        if char == '+' or char == '-':
            operatorsList.append(char)

    resultNumber = numbersList[0]
    while index < len(operatorsList):
        if operatorsList[index] == '+':
            resultNumber += numbersList[index + 1]
            index += 1
        elif operatorsList[index] == '-':
            currentNumber = numbersList[index + 1]
            index += 1
            # 55 - 50 - 40처럼 마지막에 - 들어갈때의 예외처리
            if index == len(operatorsList):
                resultNumber -= currentNumber
                currentNumber = 0
                break
            while operatorsList[index] != '-':
                currentNumber += numbersList[index + 1]
                index += 1
                # 55 - 50 + 40처럼 -로 묶인 currentNumber가 끝까지 갔을때의 예외처리
                if index == len(operatorsList):
                    break
            resultNumber -= currentNumber
            currentNumber = 0

    return resultNumber

listString = sys.stdin.readline()
print(makeProperParenthesis(listString))