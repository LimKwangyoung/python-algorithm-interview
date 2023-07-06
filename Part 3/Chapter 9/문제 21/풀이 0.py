import sys


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = ''
        letter_set = set(s)
        n = len(letter_set)

        min_idx = 0
        while len(result) != n:
            min_ascii = sys.maxsize
            for i in range(min_idx, len(s)):
                if s[i] not in result and set(s[i:]) - set(result) == letter_set and ord(s[i]) < min_ascii:
                    min_idx, min_ascii = i, ord(s[i])
            result += s[min_idx]
            letter_set.remove(s[min_idx])
            min_idx += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicateLetters('bcabc'))
    print(solution.removeDuplicateLetters('cbacdcbc'))
