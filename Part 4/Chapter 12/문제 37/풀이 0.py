class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        stack = [[i] for i in range(len(nums) - 1, -1, -1)]
        while stack:
            idx_lst = stack.pop()
            result.append([nums[i] for i in idx_lst])
            for i in range(idx_lst[-1] + 1, len(nums)):
                stack.append(idx_lst + [i])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
