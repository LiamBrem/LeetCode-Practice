"""
map {row: [reserved seats]}

add 2 * n - len(map) -> completely open rows

for row in map
calculcate max

"""
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        m = defaultdict(set)
        for row, seat in reservedSeats:
            m[row].add(seat)

        res = 0
        res += 2 * (n - (len(m)))

        for row in m.values():
            total = 0
            if 2 not in row and 3 not in row and 4 not in row and 5 not in row:
                total += 1
            if 6 not in row and 7 not in row and 8 not in row and 9 not in row:
                total  += 1
            if total == 0 and 4 not in row and 5 not in row and 6 not in row and 7 not in row:
                total += 1

            res += total

        return res 

            

                    


        