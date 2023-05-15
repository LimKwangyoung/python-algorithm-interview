class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = {}
        for word in strs:
            str_set = tuple(sorted([i for i in word]))

            if str_set in anagram_dict:
                anagram_dict[str_set].append(word)
            else:
                anagram_dict[str_set] = [word]

        return [i for i in anagram_dict.values()]


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
