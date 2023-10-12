import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        airlines = collections.defaultdict(list)
        for i, j in tickets:
            airlines[i].append(j)
        for i in airlines:
            airlines[i].sort(reverse=True)
        return airlines

        result = []
        airport = 'JFK'
        while True:
            result.append(airport)
            if not airlines[airport]:
                return result
            airport = airlines[airport].pop()


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    # print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    print(solution.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
