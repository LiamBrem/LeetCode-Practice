class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j):
            if (i, j) in seen:
                return

            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 

            seen.add((i, j))

            if grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for (dr, dc) in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                dfs(i + dr, j + dc) 


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    total += 1
                    seen = set()
                    dfs(row, col)


        return total
        