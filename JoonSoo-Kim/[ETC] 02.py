import re

def reverseStringList(stringList: list) -> list:
    return stringList[::-1]

# 투 포인터를 이용한 스왑
def reverseStringListExample01(stringList: list) -> list:
    left, right = 0, len(stringList) - 1;
    while left < right:
        stringList[left], stringList[right] = stringList[right], stringList[left]
        left += 1
        right -= 1
    return stringList

# 파이써닉 방식
def reverseStringListExample02(stringList: list) -> list:
    return stringList.reverse()


strings = input()
stringList = []

strings = re.sub(r"[^a-zA-Z0-9]", "", strings)

for char in strings:
    stringList.append(char)

print(reverseStringList(stringList))