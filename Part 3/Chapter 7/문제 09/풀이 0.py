class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:  # Time Limit Exceeded.
        nums.sort()
        # return nums
        result = []
        left, right = 0, len(nums) - 1
        while nums[left] <= 0 and left <= right - 2:
            while nums[right] >= 0 and left + 2 <= right:
                total = nums[left] + nums[right]
                if total >= 0:
                    center = left + 1
                    while nums[left] + nums[center] + nums[right] <= 0 and center < right:
                        if nums[left] + nums[center] + nums[right] == 0 and [nums[left], nums[center], nums[right]] not in result[::-1]:
                            result.append([nums[left], nums[center], nums[right]])
                            break
                        center += 1
                else:
                    center = right - 1
                    while nums[left] + nums[center] + nums[right] >= 0 and left < center:
                        if nums[left] + nums[center] + nums[right] == 0 and [nums[left], nums[center], nums[right]] not in result[::-1]:
                            result.append([nums[left], nums[center], nums[right]])
                            break
                        center -= 1
                right -= 1
            left += 1
            right = len(nums) - 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
