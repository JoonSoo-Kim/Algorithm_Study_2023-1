class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        temp_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(temp_elements[:])

            for element in elements:
                next_element = elements[:]
                next_element.remove(element)

                temp_elements.append(element)
                dfs(next_element)
                temp_elements.pop()

        dfs(nums)
        return result

s = Solution()
print(s.permute([1, 2, 3]))