class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        if len(intervals) <= 1:
            return intervals

        s = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            val = intervals[i]
            if val[0] <= s[1]:
                if val[1] > s[1]:
                    s[1] = val[1]
                if i == len(intervals) - 1:
                    res.append([s[0],s[1]])
            else:
                res.append(s)
                s = val
                if i == len(intervals) - 1:
                    res.append(intervals.pop())

        return res