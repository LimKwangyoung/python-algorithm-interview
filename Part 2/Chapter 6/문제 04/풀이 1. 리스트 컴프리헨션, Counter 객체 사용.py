import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'\W', ' ', paragraph).lower().split() if word not in banned]
        # words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        '''
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        return max(counts, key=counts.get)
        '''

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.mostCommonWord(
        paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
        banned=["hit"]
    ))
