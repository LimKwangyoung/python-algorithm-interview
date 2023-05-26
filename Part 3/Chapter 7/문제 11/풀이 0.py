class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """공간 복잡도는 O(n)."""
        results = []

        n = len(nums)
        left_lst, right_lst = [1], [1]
        for i in range(n - 1):
            left_lst.append(left_lst[-1] * nums[i])
            right_lst.append(right_lst[-1] * nums[n - 1 - i])

        for i in range(n):
            results.append(left_lst[i] * right_lst[n - 1 - i])

        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
