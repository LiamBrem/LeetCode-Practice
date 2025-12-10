"""
[4, 2, 3]
[2, 1, 1]

[2, 2, 3]

"""




class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = sorted([math.ceil(dist[i] / speed[i]) for i in range(len(dist))]) + [float('inf')]
    
        time_remaining = times[0]
        total = 0
        for i in range(len(times) - 1):
            total += 1
            time_remaining += (times[i + 1] - times[i] - 1)
            if time_remaining == 0:
                return total

        return total