import sys
from collections import deque


def get_ac_result(func: str, size: int, arr: list) -> str:
    r_num = 0
    ac_queue = deque()
    result = "["

    if func.count("D") > size:
        return "error"

    for num in arr:
        ac_queue.append(num)

    for char in func:
        if char == "R":
            r_num += 1
        if char == "D" and r_num % 2 == 0:
            ac_queue.popleft()
        if char == "D" and r_num % 2 == 1:
            ac_queue.pop()

        if len(ac_queue) == 0:
            break

    if r_num % 2 == 1:
        ac_queue.reverse()
    for _ in range(len(ac_queue)-1):
        result += str(ac_queue.popleft()) + ","
    if len(ac_queue) != 0:
        result += str(ac_queue.popleft()) + "]"
    else:
        result += "]"
    return result


t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline()[:-1]
    n = int(sys.stdin.readline())
    x_str = input().strip("[""]").split(",")

    if n == 0 and p.find("D") != -1:
        print("error")
        continue
    elif n == 0 and p.find("D") == -1:
        print("[]")
        continue

    for i in range(len(x_str)):
        x_str[i] = int(x_str[i])
    print(get_ac_result(p, n, x_str))