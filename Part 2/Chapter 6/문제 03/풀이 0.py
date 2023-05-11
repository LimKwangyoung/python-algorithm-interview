class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_lst, digit_lst = [], []
        for log in logs:
            lst = log.split()
            for i in lst[1:]:
                if i.isalpha():
                    letter_lst.append(log)
                    break
            else:
                digit_lst.append(log)

        letter_lst.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter_lst + digit_lst


if __name__ == '__main__':
    solution = Solution()
    print(solution.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
