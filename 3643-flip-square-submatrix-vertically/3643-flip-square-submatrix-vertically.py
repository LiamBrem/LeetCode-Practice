class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k):
            row = x
            endRow = x + k - 1
            col = i + y

            while row < endRow:
                tmp = grid[row][col]
                grid[row][col] = grid[endRow][col]
                grid[endRow][col] = tmp
                row += 1
                endRow -= 1




        return grid
        