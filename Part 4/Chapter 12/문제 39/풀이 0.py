import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def bfs(course: int) -> bool:
            visited = [None] * numCourses
            que = collections.deque([course])  # [course, level]
            visited[course] = 1
            while que:
                course = que.popleft()
                while graph[course]:
                    c = graph[course].pop()
                    if course == c:
                        return False
                    elif not visited[c] or visited[course] <= visited[c]:
                        que.append(c)
                        visited[c] = visited[course] + 1
                    else:
                        return False
            return True

        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)

        for i in range(numCourses):
            if not bfs(i):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
