class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sortedPoints = sorted(points, key=lambda x: x[1], reverse=True)

        res = 0

        while len(sortedPoints) > 0:
            cur = sortedPoints[-1][1]
            while len(sortedPoints) > 0 and sortedPoints[-1][0] <= cur:
                sortedPoints.pop()
            
            res += 1


        return res
        