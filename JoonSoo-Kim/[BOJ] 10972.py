import sys
input = sys.stdin.readline

def printNextPermutation(nNum: int, pList: list):
    firstIndex = 0
    secondIndex = 0

    if pList == sorted(pList, reverse=True):
        print(-1)
        return

    # 인덱스 i 구하기
    for index in range(len(pList) - 1):
        if pList[index] < pList[index+1]:
            firstIndex = index

    # 인덱스 j 구하기
    for index in range(firstIndex + 1, len(pList)):
        if pList[firstIndex] < pList[index]:
            secondIndex = index

    # i와 j를 swap
    pList[firstIndex], pList[secondIndex] = pList[secondIndex], pList[firstIndex]

    # i=1부터 reverse
    pListTwo = pList[firstIndex+1:]
    pListTwo.reverse()
    pList = pList[:firstIndex+1] + pListTwo

    print(' '.join(map(str, pList)))
    #printList(pList)

nNum = int(input())
pList = list(map(int, input().split()))
printNextPermutation(nNum, pList)