class Solution:
    def trap(self, height: list[int]) -> int:
        result, floor = 0, 0
        while True:
            left, right = 0, len(height) - 1
            while height[left] <= floor and left < len(height) - 1:
                left += 1
            while height[right] <= floor and right > 0:
                right -= 1
            if right <= left:
                break
            result += sum(height[left:right + 1].count(i) for i in range(floor + 1))
            floor += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
