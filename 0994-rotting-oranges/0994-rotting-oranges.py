"""

[[2,1,1],
 [1,1,0],
 [0,1,1]]

[[2,1,1],
 [0,1,1],
 [1,0,1]]

notes:
    - the orange with the furthest distance from a rotten orange will be the last to rot
    - the time it will take to rot IS the distance
    - if any orange is not adjacent to any other orange -> never rots -> return -1
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        farthest = 0
        hasRot = False
        hasOrange = False
        visited = set()

        def isIsolated(row, col):
            if row - 1 >= 0 and grid[row - 1][col] != 0:
                return False
            if row + 1 < rows and grid[row + 1][col] != 0:
                return False
            if col - 1 >= 0 and grid[row][col - 1] != 0:
                return False
            if col + 1 < cols and grid[row][col + 1] != 0:
                return False

            return True

        def findClosestRot(row, col, dist):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return float('inf')
            if grid[row][col] == 0:
                return float('inf')
            if (row, col) in visited:
                return float('inf')
            if grid[row][col] == 2:
                return dist 

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            minDist = float('inf')

            visited.add((row, col))

            for d in dirs:
                minDist = min(minDist, findClosestRot(row + d[0], col + d[1], dist + 1))

            visited.remove((row, col))
            return minDist


        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    hasOrange = True
                    farthest = max(farthest, findClosestRot(row, col, 0))
                    if farthest == float('inf'):
                        return -1

                elif grid[row][col] == 2:
                    hasRot = True

        if hasOrange and not hasRot:
            return -1

        return farthest