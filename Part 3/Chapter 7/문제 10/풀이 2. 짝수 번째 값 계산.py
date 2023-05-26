class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sums = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sums += n

        return sums


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrayPairSum([1, 4, 3, 2]))
