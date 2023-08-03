class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        for i, temp in enumerate(temperatures[1:]):
            while stack and stack[-1][0] < temp:
                j = stack.pop()[1]
                result[j] = (i + 1) - j
            stack.append((temp, i + 1))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
