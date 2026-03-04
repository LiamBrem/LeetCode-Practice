"""
[1, 3] [2, 6] [8, 10] [15, 18]

[1, 6] [8, 10] [15, 18]



"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        count = 0

        for start, end in intervals:
            if not res:
                res.append([start,end])
                continue 

            cap = res[-1][1]
            if start > cap:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)
        

        return res