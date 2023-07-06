class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for i in s:
            if i in bracket:  # open bracket
                stack.append(i)
            elif not stack or i != bracket[stack.pop()]:  # close bracket
                return False
        return not stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()[]{}'))
