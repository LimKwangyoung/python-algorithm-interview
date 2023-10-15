import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:  # wrong answer
        airlines = collections.defaultdict(list)
        for i, j in tickets:
            airlines[i].append(j)
        for i in airlines:
            airlines[i].sort(reverse=True)

        path = ['JFK']
        airport = path[-1]
        destination = ''
        while airlines[airport]:
            if airlines[airport] and airlines[airlines[airport][-1]]:
                path.append(airlines[airport].pop())
                airport = path[-1]
            elif not destination:
                destination = airlines[airport].pop()
            else:
                path.append(airlines[airport].pop())
                airport = path[-1]

        return path + [destination]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
