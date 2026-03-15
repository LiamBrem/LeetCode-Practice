class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        highest = 0
        winner = -1
        for i, li in enumerate(grid):
            ones = li.count(1)
            if ones > highest:
                highest = ones
                winner = i

        return winner

        