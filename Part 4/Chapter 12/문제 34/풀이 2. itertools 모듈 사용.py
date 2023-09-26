import itertools


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(map(list, itertools.permutations(nums)))


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
