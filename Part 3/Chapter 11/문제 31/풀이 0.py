import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_dict = collections.Counter(nums).most_common()
        lst = [nums_dict[i][0] for i in range(k)]

        return lst


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
