import sys
from collections import deque
input = sys.stdin.readline

def get_right_big(size:int, numbers:list) -> list:
    num_stack = deque()
    result_list = [-1 for _ in range(size)]

    for i in range(size):
        while num_stack and num_stack[-1][0] < numbers[i]:
            temp, index = num_stack.pop()
            result_list[index] = numbers[i]
        num_stack.append([numbers[i], i])

    return result_list


n = int(input())
a_list = list(map(int, input().split()))

result = get_right_big(n, a_list)
for i in range(len(result)-1):
    print(result[i], end=" ")
print(result[-1], end="")

