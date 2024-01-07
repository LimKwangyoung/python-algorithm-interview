import collections
import sys


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        que = collections.deque([k])
        visited = [None] * (n + 1)
        visited[k] = 0
        while que:
            u = que.popleft()
            for v, w in graph[u]:
                if visited[v] is None or visited[u] + w < visited[v]:
                    visited[v] = visited[u] + w
                    que.append(v)

        result = -sys.maxsize
        for i in visited[1:]:
            if i is None:
                return -1
            result = max(result, i)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
