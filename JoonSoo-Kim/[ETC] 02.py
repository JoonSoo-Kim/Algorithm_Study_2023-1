import re

def reverseStringList(stringList: list) -> list:
    return stringList[::-1]


strings = input()
stringList = []

strings = re.sub(r"[^a-zA-Z0-9]", "", strings)

for char in strings:
    stringList.append(char)

print(reverseStringList(stringList))