# AAABBB - 불가능
# 홀수개의 알파벳이 2개 이상이면 불가능하다
# 홀수개의 알파벳이 존재한다면, 그 값은 중앙에 하나가 무조건 들어가야 한다
import sys
input = sys.stdin.readline()

alphabet_list = list(input.strip())
alphabet_list.sort(reverse=True)
counter = {}
for alphabet in alphabet_list:
    if alphabet in counter:
        counter[alphabet] += 1
    else:
        counter[alphabet] = 1

mid = '' # 홀수개의 알파벳 value
result = '' # 출력값
danger = 0 # 홀수개의 알파벳 개수 (danger >= 2 이면 불가능)
for value in counter:
    if counter[value] % 2 == 1:
        danger += 1
        if danger == 2:
            break
        mid = value
        counter[value] -= 1
    result = value*(counter[value] // 2) + result + value*(counter[value] // 2)

if danger == 2:
    print("I'm Sorry Hansoo")
else:
  if mid != '':
      result = result[:len(result) // 2] + mid + result[len(result) // 2 :]
  print(result)
