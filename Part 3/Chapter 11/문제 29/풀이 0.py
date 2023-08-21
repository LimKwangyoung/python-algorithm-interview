import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = collections.Counter(stones)
        cnt = 0
        for i in jewels:
            cnt += stones_dict[i]
        return cnt


if __name__ == '__main__':
    solution = Solution()
    print(solution.numJewelsInStones('aA', 'aAAbbbb'))
