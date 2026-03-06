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
        rows, cols = len(grid), len(grid[0])
        dists = [[float('inf')] * cols for _ in range(rows)]
        q = deque()
        anyOranges = False
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    anyOranges = True
                if grid[row][col] == 2:
                    q.append((row, col, 0))

        if not anyOranges:
            return 0 

        while q:
            row, col, dist = q.popleft()
            dists[row][col] = min(dists[row][col], dist)

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newRow = row + dr
                newCol = col + dc
                if newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    q.append((newRow, newCol, dist + 1))

        res = -1
        for row in range(rows):
            for col in range(cols):
                if dists[row][col] != float('inf'):
                    res = max(res, dists[row][col])

                elif grid[row][col] == 1: # unrotten orange, unreached by bfs
                    return -1


        return res
                    


                                    