import collections


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u].append([v, w])

        que = collections.deque([k])
        visited = [False] * (n + 1)
        visited[k] = 0
        while que:
            u = que.popleft()
            for v, w in nodes[u]:
                if v != k:
                    if visited[v]:
                        visited[v] = min(visited[v], visited[u] + w)
                    else:
                        visited[v] = visited[u] + w
                    que.append(v)

        for i in visited[1:]:
            if i is False:
                return -1
        else:
            return max(visited[1:])


if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime(times=[[1, 2, 1], [2, 1, 3]], n=2, k=2))
