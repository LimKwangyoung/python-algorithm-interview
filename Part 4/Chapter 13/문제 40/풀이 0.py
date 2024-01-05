import collections


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u].append([v, w])

        cnt = 0
        que = collections.deque([k])
        visited = [False] * (n + 1)
        visited[k] = True
        while que:
            vertex = que.popleft()
            for i in range(len(nodes[vertex])):
                if nodes[vertex][i][1] >= 1:
                    nodes[vertex][i][1] -= 1
                    if nodes[vertex][i][1] == 0:
                        que.append(nodes[vertex][i][0])
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
