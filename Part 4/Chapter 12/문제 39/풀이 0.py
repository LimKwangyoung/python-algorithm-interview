import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        def dfs(course: int) -> bool:
            visited = set()
            stack = [course]
            while stack:
                course = stack.pop()
                if course in visited:
                    return False

                visited.add(course)
                if not graph[course]:
                    visited = set()
                else:
                    for c in graph[course]:
                        stack.append(c)
            return True

        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)

        for i in range(numCourses):
            if graph[i] and not dfs(i):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    # print(solution.canFinish(2, [[1, 0]]))
    # print(solution.canFinish(2, [[1, 0], [0, 1]]))
    # print(solution.canFinish(5, [[0, 1], [0, 2], [2, 1], [1, 3], [2, 3], [3, 4], [4, 2]]))
    print(solution.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))
