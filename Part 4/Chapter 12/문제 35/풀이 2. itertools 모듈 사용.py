import itertools


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return list(map(list, itertools.combinations(range(1, n + 1), k)))


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(n=4, k=2))
