class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0

        buy = 0
        while buy <= len(prices) - 2:
            while buy <= len(prices) - 2 and prices[buy] >= prices[buy + 1]:
                buy += 1
            sell = buy + 1
            while sell <= len(prices) - 1 and prices[buy] <= prices[sell]:
                result = max(result, prices[sell] - prices[buy])
                sell += 1
            buy = sell
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
