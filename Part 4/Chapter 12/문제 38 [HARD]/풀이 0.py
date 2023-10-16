import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        airlines = collections.defaultdict(list)
        for i, j in tickets:
            airlines[i].append(j)
        for i in airlines:
            airlines[i].sort(reverse=True)

        stack = ['JFK']
        result = []
        while stack:
            airport = stack[-1]
            if airlines[airport]:
                stack.append(airlines[airport].pop())
            else:
                result.append(stack.pop())
        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
