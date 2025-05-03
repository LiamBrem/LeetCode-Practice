class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        minimum = float('inf')

        r1 = r2 = 0
        for i in range(len(grid[0])):
            r1 += grid[0][i]
        
        for i in range(len(grid[0])):
            r1 -= grid[0][i]
            minimum = int(min(minimum, max(r1, r2)))
            r2 += grid[1][i]

        return minimum
