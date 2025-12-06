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
        rows, cols = len(grid), len(grid[0])

        def isInBounds(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols

        def findClosestRot(row, col, dist):
            q = deque()
            visited = set()
            q.append((row, col, 0))

            while q:
                row, col, dist = q.popleft()
                if (row, col) in visited:
                    continue 
                visited.add((row, col))

                for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newRow = row + d[0]
                    newCol = col + d[1]
                    if isInBounds(newRow, newCol) and (newRow, newCol) not in visited and grid[newRow][newCol] != 0:
                        if grid[newRow][newCol] == 2:
                            return 1 + dist
                        q.append((newRow, newCol, dist + 1))

            return float('inf')


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