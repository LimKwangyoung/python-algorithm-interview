class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        height, width = len(grid), len(grid[0])

        def dfs():
            row, col = stack.pop()
            if col < width - 1 and grid[row][col + 1] == '1':
                grid[row][col + 1] = '0'
                stack.append((row, col + 1))
            if row < height - 1 and grid[row + 1][col] == '1':
                grid[row + 1][col] = '0'
                stack.append((row + 1, col))
            if col > 0 and grid[row][col - 1] == '1':
                grid[row][col - 1] = '0'
                stack.append((row, col - 1))
            if row > 0 and grid[row - 1][col] == '1':
                grid[row - 1][col] = '0'
                stack.append((row - 1, col))

        result = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    result += 1
                    stack = [(i, j)]
                    while stack:
                        dfs()
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]))
    print(solution.numIslands([
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]))
