def solution(participant, completion):
    participant.sort()
    completion.sort()

    answer = participant[-1]

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    return answer