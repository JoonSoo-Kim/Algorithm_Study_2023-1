def solution(numbers, target):
    answer = 0
    temp_exp = []
    answer_list = []

    def dfs(nums):
        nonlocal answer, target
        if len(nums) == 0:
            if sum(temp_exp) == target:
                print(temp_exp, "1번통과")
                if answer_list.count(temp_exp) == 0:
                    print(temp_exp, "2번통과")
                    answer_list.append(temp_exp)
                    answer += 1
            return

        for num in nums:
            for sign in [+1, -1]:
                next_nums = nums[:]
                next_nums.remove(num)
                num *= sign
                temp_exp.append(num)
                dfs(next_nums)
                temp_exp.pop()

    dfs(numbers)

    print(answer)
    return answer

solution([1, 1, 1, 1, 1], 3)
