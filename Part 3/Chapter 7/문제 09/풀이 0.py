class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if (-1) * (nums[i] + nums[j]) in nums[j + 1:]:
                    lst = [nums[i], nums[j], (-1) * (nums[i] + nums[j])]
                    for k in result:
                        if set(lst) == set(k):
                            break
                    else:
                        result.append(lst)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
