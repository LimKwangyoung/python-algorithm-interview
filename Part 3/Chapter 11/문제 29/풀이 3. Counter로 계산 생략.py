import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)  # 돌(S) 빈도 수 계산
        count = 0

        # 비교 없이 보석(J) 빈도 수 합산
        for char in jewels:
            count += freqs[char]

        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numJewelsInStones('aA', 'aAAbbbb'))
