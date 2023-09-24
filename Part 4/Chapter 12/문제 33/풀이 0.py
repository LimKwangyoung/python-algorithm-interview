class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        result = []
        if not digits:
            return result

        stack = [i for i in letters_dict[digits[0]]]
        while stack:
            string = stack.pop()
            if len(string) == len(digits):
                result.append(string)
                continue

            for i in letters_dict[digits[len(string)]]:
                stack.append(string + i)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
