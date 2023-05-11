# boj 15686
# 모든 가능한 치킨집 조합에 대해 각각의 치킨 거리를 구해서 최소값 출력
import sys
from itertools import combinations

# 입력값
n, m = map(int, sys.stdin.readline().split())
temp_list, home_list, chicken_list = [], [], []  # 임시 리스트, 집, 치킨집의 위치를 저장할 리스트

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))  # 각 행을 입력받아 리스트로 변환
    temp_list.append(row)  # 일단 임시 리스트에 각 행을 추가
    for j in range(n):
        if row[j] == 1:  # 집인 경우 home_list에 추가
            home_list.append((i, j))
        elif row[j] == 2:  # 치킨집인 경우 chicken_list에 추가
            chicken_list.append((i, j))


# 치킨집 조합 만들기
chickenCombi = list(combinations(range(len(chicken_list)), m))

# 치킨 거리 계산하기
result = 999999999  # 결과값(도시의 치킨거리의 최소값) 초기화
for cList in chickenCombi:  # 치킨집 조합마다
    total_dist = 0  # 도시 치킨 거리값 초기화
    for home in home_list:  # 집마다
        ch_dist = 999999999 # 가장 가까운 치킨 거리 구하기
        for ch in cList:  # 치킨집 조합 중 하나의 치킨집 마다
            dist = abs(home[0] - chicken_list[ch][0]) + abs(home[1] - chicken_list[ch][1])  # 집까지의 거리 계산
            ch_dist = min(ch_dist, dist)  # 한 집의 치킨 거리 결정
        total_dist += ch_dist  # 각 집들의 치킨 거리들의 합
    result = min(result, total_dist)  # 도시 치킨 거리의 최소값 결정

# 결과 출력
print(result)
