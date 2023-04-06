import sys
from collections import deque
input = sys.stdin.readline

def is_valid_p(parentheses: str) -> bool:
    stack = deque()

    for p in parentheses:
        if len(stack) == 0:
            stack.append(p)
            continue

        if stack[-1] == "(" and p == ")":
            stack.pop()
            continue
        if stack[-1] == "{" and p == "}":
            stack.pop()
            continue
        if stack[-1] == "[" and p == "]":
            stack.pop()
            continue

        stack.append(p)

    if len(stack) == 0:
        return True
    else:
        return False

def is_valid_p_1(s: str) -> bool:
    stack = deque()
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0


s = "()[]{}"
print(is_valid_p_1(s))