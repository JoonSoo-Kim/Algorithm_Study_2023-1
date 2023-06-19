import sys
input = sys.stdin.readline

N = int(input())
dices = []
for _ in range(N):
    dices.append(list(map(int, input().split())))
match = {0: 5, 5: 0, 1: 3, 3: 1, 2: 4, 4: 2}

maximum_num = -1
for i in range(6):
    result = []
    num_list_first = [1, 2, 3, 4, 5, 6]
    top = dices[0][match[i]]
    # num_list_first에서 위 아래 값 제거
    num_list_first.remove(dices[0][i])
    num_list_first.remove(top)
    # 남아있는 옆면 중 가장 큰 수를 result에 더함
    result.append(max(num_list_first))

    # 1번째 주사위부터 마지막 주사위까지 쌓음
    for j in range(1, N):
        num_list_next = [1, 2, 3, 4, 5, 6]
        # top값과 매치되는 값의 인덱스를 찾아서 다음 주사위의 top을 찾음
        top_next = dices[j][match[dices[j].index(top)]]
        num_list_next.remove(top)
        num_list_next.remove(top_next)
        top = top_next
        result.append(max(num_list_next))

    if maximum_num < sum(result):
        maximum_num = sum(result)

print(maximum_num)
