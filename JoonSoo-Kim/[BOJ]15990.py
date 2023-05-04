import sys
input = sys.stdin.readline
DIV = 1000000009

sum_list = [[0] * 4 for _ in range(1000001)]
sum_list[1] = [0, 1, 0, 0] # 1 : 1
sum_list[2] = [0, 0, 1, 0] # 2 : 2
sum_list[3] = [0, 1, 1, 1] # 3: 12 21 3

for i in range(4, 1000001):
    # i-1에서 2와 3으로 끝난 수에 +1 붙여서 i 만들기
    sum_list[i][1] = (sum_list[i-1][2] + sum_list[i-1][3]) % DIV
    # i-2에서 1과 3으로 끝난 수에 +2 붙여서 i 만들기
    sum_list[i][2] = (sum_list[i-2][1] + sum_list[i-2][3]) % DIV
    # i-3에서 1과 2로 끝난 수에 +3 붙여서 i 만들기
    sum_list[i][3] = (sum_list[i-3][1] + sum_list[i-3][2]) % DIV


t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(sum_list[n]) % DIV)


