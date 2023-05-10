class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == '__main__':
    solution = Solution()
    solution.reverseString(['h', 'e', 'l', 'l', 'o'])
    solution.reverseString(['H', 'a', 'n', 'n', 'a', 'h'])
