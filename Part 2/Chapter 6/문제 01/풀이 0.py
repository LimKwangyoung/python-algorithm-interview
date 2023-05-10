class Solution:
    def isPalindrome(self, s: str) -> bool:
        character_lst = []
        for i in s:
            if i.isalnum():
                character_lst.append(i)

        left, right = 0, len(character_lst) - 1
        while left < right:
            if character_lst[left].lower() != character_lst[right].lower():
                return False
            left += 1
            right -= 1
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
