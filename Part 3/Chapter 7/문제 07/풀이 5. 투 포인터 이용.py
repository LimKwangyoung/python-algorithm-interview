class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """nums 리스트가 정렬되어 있어야 한다."""
        left, right = 0, len(nums) - 1
        while not left == right:
            # 합이 타켓보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타켓보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
