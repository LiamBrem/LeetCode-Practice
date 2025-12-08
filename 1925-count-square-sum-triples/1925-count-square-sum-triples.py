class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n):
            for j in range(i, n):
                num = (i**2 + j**2)**0.5
                if num <= n and num.is_integer():
                    res += 2


        return res