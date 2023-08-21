class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numJewelsInStones('aA', 'aAAbbbb'))
