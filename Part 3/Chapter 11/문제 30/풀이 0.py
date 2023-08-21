class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            letter_set = set(s[i])
            idx = 1
            while i + idx < len(s) and s[i + idx] not in letter_set:
                letter_set.add(s[i + idx])
                idx += 1
            cnt = max(cnt, idx)

        return cnt


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('bbbbb'))
    print(solution.lengthOfLongestSubstring('pwwkew'))
