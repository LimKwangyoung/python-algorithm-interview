import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for start, end, weight in flights:
            graph[start][end] = weight

        que = collections.deque([(src, 0)])  # (vertex, distance)
        visited = [None] * n
        visited[src] = 0
        for _ in range(k + 1):
            temp = collections.deque([])
            while que:
                vertex, distance = que.popleft()
                for v in graph[vertex]:
                    if not visited[v] or distance + graph[vertex][v] < visited[v]:
                        visited[v] = distance + graph[vertex][v]
                        temp.append((v, distance + graph[vertex][v]))
            que = temp

        return visited[dst] if visited[dst] else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
