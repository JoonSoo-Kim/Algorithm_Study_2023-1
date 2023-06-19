def solution(nums):
    n = len(nums) / 2
    nums_set = set(nums)

    if n <= len(nums_set):
        answer = n
    else:
        answer = len(nums_set)

    return answer