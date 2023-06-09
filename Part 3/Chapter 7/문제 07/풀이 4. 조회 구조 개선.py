class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
