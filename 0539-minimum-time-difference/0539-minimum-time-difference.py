class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(string):
            l = string.split(":")
            hrs = int(l[0])
            mins = int(l[1])
            return hrs * 60 + mins

        timePoints = sorted(timePoints)

        minimum = float('inf')
        timePointsInt = []

        for timePoint in timePoints:
            timePointsInt.append(convert(timePoint))

        for i in range(1, len(timePointsInt)):
            minimum = min(minimum, timePointsInt[i]-timePointsInt[i-1])

        return min(minimum, (24*60) + timePointsInt[0] - timePointsInt[-1])
            












    
