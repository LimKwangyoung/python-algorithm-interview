class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n, 0, -1):
            for j in range(n):
                if i + j > n:
                    break
                string = s[j:j + i]
                if string == string[::-1]:
                    return string


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("babad"))
    print(solution.longestPalindrome("cbbd"))
