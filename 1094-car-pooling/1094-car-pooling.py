"""
[1, 2]
[3, 7]

[x, (f 2), (f 3), t, x, x, x, t 2, x, x, x, x, x, x]

"""
class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool: 
        froms = sorted(trips, key=lambda x: x[1])
        tos = sorted(trips, key=lambda x: x[2])

        arr = [0] * (tos[-1][2] + 1)

        for to in tos:
            arr[to[2]] = -to[0]

        for f in froms:
            arr[f[1]] = f[0]

        currCapacity = 0

        for val in arr:
            currCapacity += val
            if currCapacity > capacity:
                return False

        return True
            
