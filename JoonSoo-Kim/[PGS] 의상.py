from itertools import combinations


def solution(clothes):
    answer = 0

    # 옷의 종류 찾기
    clothes_type = set()
    for c in clothes:
        clothes_type.add(c[1])
    clothes_type = list(clothes_type)

    # 옷 30개가 각각 종류가 전부 다른 경우 2^30 - 1
    if len(clothes_type) == 30:
        return 1073741823

    # 각 종류 별 옷 개수 세기
    clothes_num = [0] * len(clothes_type)
    for c in clothes:
        for i in range(len(clothes_type)):
            if c[1] == clothes_type[i]:
                clothes_num[i] += 1

    for i in range(1, len(clothes_type) + 1):
        clothes_comb = list(combinations(clothes_type, i))
        # 각 combination에 대해 clothes_num만큼 곱해서 answer에 더해줌
        for comb in clothes_comb:
            comb = list(comb)
            temp = 1
            for index in comb:
                temp *= clothes_num[clothes_type.index(index)]
            answer += temp

    return answer