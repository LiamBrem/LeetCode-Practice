"""
1
5
13
25

Edges:
1
4
8
12
16


"""
class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        edges = 0
        for i in range(n):
            res += edges
            edges += 4

        return res
        