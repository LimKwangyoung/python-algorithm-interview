class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(lst: list[int], idx: int, t: int) -> None:
            if sum(lst) == t:
                result.append(lst)

            for i in range(idx, len(candidates)):
                elements = lst[:]
                for j in range((target - sum(lst)) // candidates[i]):
                    elements.append(candidates[i])
                    dfs(elements, i + 1, target - sum(elements))
        result = []
        dfs([], 0, target)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([2, 3, 5], 8))