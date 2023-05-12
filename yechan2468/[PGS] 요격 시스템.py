def solution(targets):
    answer = 0
    
    # 같은 start에서 시작하는 중복을 제거하고, 형태 만들어주기
    targets.sort(key=lambda x: x[0])
    targets.sort(key=lambda x: x[1])
    targets = dict(map(lambda x: [x[1], x[0]], targets))

    prev_start, prev_end = -1, -1    
    for end in targets.keys():
        curr_start, curr_end = targets[end], end
        if (duplicated := curr_start < prev_start) or (intercepted := curr_start < prev_end):
            continue
        prev_start, prev_end = curr_start, curr_end
        answer += 1
    
    return answer


# 생각을 다시 정리

def solution(targets):
    answer = 0

    # a <= b <= c <= d 일 때 (b, c) 미사일을 요격하면 (a, d) 미사일도 요격됨
    # 반드시 모든 미사일은 명중되어야 함

    # 같은 start에서 시작하는 미사일이 여러 개 있을 때, 그 중 범위가 가장 좁은 것만을 선택해 중복을 줄임 (dict)
    targets.sort(key=lambda x: x[0])
    # end로 정렬
    targets.sort(key=lambda x: x[1])
    # start와 end의 위치를 서로 바꿔, end로 start를 접근할 수 있도록 함
    targets = dict(map(lambda x: [x[1], x[0]], targets))

    prev_end = -1
    for end in targets.keys():
        curr_start, curr_end = targets[end], end
        # intercepted: 아래 경우들과 같이, 이미 요격된 경우
        #
        # prev ----
        # curr   -------
        #         ^
        #
        # prev   ----
        # curr ---------
        #           ^
        if (intercepted := curr_start < prev_end):
            continue
        prev_end = curr_end
        answer += 1

    return answer

# 코드 정리

def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])

    prev_end = -1
    for start, end in targets:
        if start < prev_end:
            continue
        prev_end = end
        answer += 1

    return answer
