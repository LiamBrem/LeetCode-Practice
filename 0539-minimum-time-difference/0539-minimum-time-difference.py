class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(string):
            l = string.split(":")
            hrs = int(l[0])
            mins = int(l[1])
            return hrs * 60 + mins

        timePoints = sorted(timePoints)
        times = []
        for time in timePoints:
            times.append(convert(time))

        minimum = float('inf')
        for i in range(1, len(times)):
            minimum = min(minimum, times[i] - times[i-1])

        minimum = min(minimum, (24*60) + times[0] - times[-1])
        return minimum









    
