"""
x = 

"""


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n == 1:
            return 1
        res = 0
        k = 1
        while (k * (k - 1)//2) < n:
            x = (k * (k - 1) / 2 - n) / k
            if x.is_integer():
                res += 1
            k += 1

        return res
        