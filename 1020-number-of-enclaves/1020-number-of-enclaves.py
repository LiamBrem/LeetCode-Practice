class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        seen = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                    return 

            grid[row][col] = 0
            for dr, dc in dirs:
                dfs(row + dr, col + dc)

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or col == 0 or row == rows - 1 or col == cols - 1) and grid[row][col] == 1:
                    dfs(row, col)

        res = 0
        for row in range(rows):
            for col in range(cols):
                res += grid[row][col]

        return res
