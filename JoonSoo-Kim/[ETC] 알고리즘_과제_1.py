import random
import time

def bubbleSort(numList: list) -> list:
    # 리스트의 크기만큼 반복
    for i in range(len(numList)):
        # 총 크기에서 i + 1만큼 빼서 반복
        for numIndex in range(len(numList) - i - 1):
            # 이전 아이템이 그 다음 아이템보다 크다면 위치 변경
            if numList[numIndex] > numList[numIndex + 1]:
                numList[numIndex], numList[numIndex + 1] = numList[numIndex + 1], numList[numIndex]

    return numList


def quickSort(numbers: list, lowIndex: int, highIndex: int) -> list:
    # pivotIndex 초기화
    pivotIndex = -1

    # 파라미터가 제대로 왔나 확인
    if(highIndex > lowIndex):

        # pivot값을 맨 처음값인 lowIndex 값으로 초기화
        pivot = numbers[lowIndex]
        # pivot의 Index를 현재 pivot 값의 index인 lowIndex로 초기화
        pivotIndex = lowIndex

        # pivot의 시작점이 lowIndex니까 lowIndex+1부터 highIndex까지 반복해서 확인
        # pivot값보다 작은 값을 정렬
        for index in range(lowIndex + 1, highIndex + 1):
            # 해당 number가 pivot값보다 작은 경우 pivot과 위치 변경
            if(numbers[index] < pivot):
                # pivotIndex을 뒤로 1 땡김
                pivotIndex += 1
                # pivot 값은 초기 위치인 lowIndex에 그대로 둔다
                # pivotIndex의 값와 작은 값을 교환한다.
                tempNumber = numbers[index]
                numbers[index] = numbers[pivotIndex]
                numbers[pivotIndex] = tempNumber

        # pivot과 가장 낮아야 할 값인 현재 privotIndex의 값을 교환한다.
        # 이를 통해 lowIndex부터 pivotIndex까지 정렬완료
        tempNumber = numbers[lowIndex]
        numbers[lowIndex] = numbers[pivotIndex]
        numbers[pivotIndex] = tempNumber

        # pivotIndex를 기준으로 리스트를 반으로 나누어서 2개의 리스트에 대해 퀵 정렬을 반복한다
        quickSort(numbers, lowIndex, pivotIndex - 1)
        quickSort(numbers, pivotIndex + 1, highIndex)


# n을 통해 데이터 개수 조절
n = 80000
numbers = []

for i in range(n):
    # 1에서 1000 사이의 자연수를 random으로 생성
    numbers.append(random.randrange(1, 1001))

# 정렬 전후 시간 측정
startTime = time.time()
# bubbleSort(numbers)
quickSort(numbers, 0, 79999)
endTime = time.time()

print(endTime - startTime)
print(numbers)