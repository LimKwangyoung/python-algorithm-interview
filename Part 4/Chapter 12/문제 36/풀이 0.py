class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(nums: list, idx: int, t: int) -> None:
            if t == 0:
                return result.append(nums)
            elif t > 0:
                for i in range(idx, len(candidates)):
                    dfs(nums + [candidates[i]], i, t - candidates[i])

        result = []
        dfs([], 0, target)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([2, 3, 5], 8))
