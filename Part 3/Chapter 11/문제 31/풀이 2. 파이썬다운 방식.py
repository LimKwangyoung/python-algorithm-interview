import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
