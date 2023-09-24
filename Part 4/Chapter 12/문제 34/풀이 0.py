class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(idx: list[int], lst: list[int]) -> None:
            if len(idx) == 1:
                lst.append(nums[idx[0]])
                result.append(lst)
                return

            for i in range(len(idx)):
                dfs(idx[:i] + idx[i + 1:], lst + [nums[idx[i]]])

        result = []
        dfs(list(range(len(nums))), [])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
