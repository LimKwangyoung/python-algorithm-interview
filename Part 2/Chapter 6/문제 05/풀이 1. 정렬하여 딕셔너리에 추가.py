import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagram_dict[''.join(sorted(word))].append(word)
        return list(anagram_dict.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
