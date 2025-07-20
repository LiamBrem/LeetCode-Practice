class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if r >= rows or r < 0 or c >= cols or c < 0 or (r, c) in visited or grid[r][c] == "0":
                return 

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    numIslands += 1
                    dfs(row, col)                   
                
        return numIslands