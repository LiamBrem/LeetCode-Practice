class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calcTime(p1, p2):
            dx, dy = abs(p2[0] - p1[0]), abs(p2[1] - p1[1])
            return min(dx, dy) + abs(dx - dy)


        res = 0
        for i in range(len(points) - 1):
            res += calcTime(points[i], points[i + 1])

        return res
        