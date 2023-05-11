import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        word_lst = re.split('[^a-zA-Z]', paragraph.lower())

        word_set = list(set(word_lst))
        maximum, max_idx = 0, 0
        for idx in range(len(word_set)):
            if word_set[idx] in banned or word_set[idx] == '':
                continue
            if word_lst.count(word_set[idx]) > maximum:
                maximum = word_lst.count(word_set[idx])
                max_idx = idx

        return word_set[max_idx]

if __name__ == '__main__':
    solution = Solution()
    print(solution.mostCommonWord(
        paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
        banned=["hit"]
    ))
