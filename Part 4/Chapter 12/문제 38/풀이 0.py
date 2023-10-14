import collections


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        airlines = collections.defaultdict(list)
        for i, j in tickets:
            airlines[i].append(j)
        for i in airlines:
            airlines[i].sort(reverse=True)
        # return airlines

        path = ['JFK']
        destination = ''
        while True:
            airport = path[-1]
            if not airlines[airport]:
                break
            elif airlines[airlines[airport][-1]]:
                path.append(airlines[airport].pop())
            else:
                destination = airlines[airport].pop()

# import collections
# class Solution:
#     def findItinerary(self, tickets: list[list[str]]) -> list[str]:
#         graph = collections.defaultdict(list)
#         tickets.sort(key = lambda x : x[1], reverse = True)
#         for src, dst in tickets:
#           graph[src].append(dst)
#
#         res, stack = [], ['JFK']
#         while stack:
#           if stack[-1] in graph and graph[stack[-1]]:
#             stack.append(graph[stack[-1]].pop())
#
#           else:
#             res.append(stack.pop())
#
#         return res[::-1]



if __name__ == '__main__':
    solution = Solution()
    # print(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    # print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    print(solution.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
