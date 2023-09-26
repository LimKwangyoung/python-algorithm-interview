class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def dfs(lst: list, num: int, kk: int):
            if kk == 0:
                result.append(lst)
                return

            for i in range(num, n + 1):
                dfs(lst + [i], i + 1, kk - 1)

        result = []
        dfs([], 1, k)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(n=4, k=2))
