'''
input: 2d array heights
output: 2d array - cells where water can flow to both oceans

notes:
    - pacific touches l & t
    - atlantic touches r & b
    - heights[r][c] = height above sea level
    - rain can flow to adjacent cells if water <= current height
    - water can flow from any border cell into the ocean
    - return 2d array of coordinates:
        - result[i] = [r, c], rain water can flow from cell (r, c) to BOTH pacific & atlantic

edge cases: 
    - not square
    - m and n will always be > 1
    - result list can be returned in any order

strategy:
    - loop through every cell & check whether it can flow to both p & a
    - if it can, add it's coordinates to our list
    - to check if a square can flow to both -> perform dfs
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]


        def dfs(row, col, prevHeight, seen):
            if row < 0 or row >= rows or col < 0 or col >= cols or seen[row][col] or heights[row][col] < prevHeight:
                return

            seen[row][col] = True

            for dr, dc in dirs:
                dfs(row + dr, col + dc, heights[row][col], seen)


        for i in range(cols):
            dfs(0, i, 0, pacific)
            dfs(rows - 1, i, 0, atlantic)

        for i in range(rows):
            dfs(i, 0, 0, pacific)
            dfs(i, cols - 1, 0, atlantic)


        res = []

        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    res.append([row, col])

        return res

        