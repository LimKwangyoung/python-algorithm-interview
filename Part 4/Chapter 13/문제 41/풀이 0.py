import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for start, end, weight in flights:
            graph[start][end] = weight

        que = [(0, src, 0)]  # (distance, vertex, stopover)
        visited = collections.defaultdict(list)
        while que:
            distance, start, stopover = heapq.heappop(que)
            if stopover <= k + 1:
                # visited[start][distance] = stopover
                visited[start].append(distance)
                for end in graph[start]:
                    heapq.heappush(que, (distance + graph[start][end], end, stopover + 1))
        # print(visited)
        return min(visited[dst]) if dst in visited else -1
        # return visited[dst] if dst in visited else -1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
    print(solution.findCheapestPrice(n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1))
