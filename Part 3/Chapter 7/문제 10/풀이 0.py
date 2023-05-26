class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        result = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            result += nums[i]

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrayPairSum([1, 4, 3, 2]))
