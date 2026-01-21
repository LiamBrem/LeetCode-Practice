class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        rowDiff, colDiff = (homePos[0] - startPos[0]), (homePos[1] - startPos[1])
        res = 0

        if rowDiff > 0:
            res += sum(rowCosts[startPos[0] + 1:homePos[0] + 1])
        elif rowDiff < 0:
            res += sum(rowCosts[homePos[0]: startPos[0]])


        if colDiff > 0:
            res += sum(colCosts[startPos[1]+ 1: homePos[1] + 1])
        elif colDiff < 0:
            res += sum(colCosts[homePos[1]: startPos[1]])


        return res