import sys
input = sys.stdin.readline

def isCommonString(nNumber: int, mNumber: int) -> int:
    resultNumber = 0
    nSet = set()
    mString = ""

    # 셋과 딕셔너리는 해시 테이블 구조로 되어있어 리스트보다 탐색이 빠르다
    for _ in range(nNumber):
        nSet.add(input())
    # n과 m을 1대1로 비교하면 매우 오래 걸린다.
    # 따라서 mStringList를 애초에 만들지 않고 바로 비교해서 m의 탐색 시간을 없앤다.
    for _ in range(mNumber):
        mString = input()
        if mString in nSet:
            resultNumber += 1

    return resultNumber


nNumber, mNumber = map(int, input().split())

print(isCommonString(nNumber, mNumber))