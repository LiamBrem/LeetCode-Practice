"""
4 3 2 1

4 3 2 1 43 32 21 432 321 4321


"""
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        def getNum(n):
            return (n * (n + 1)) // 2

        res = 0
        i = 0

        while i < len(prices):
            size = 1
            j = i + 1
            prev = i
            while j < len(prices) and prices[prev] - prices[j] == 1:
                size += 1
                j += 1
                prev += 1

            res += getNum(size)
            i = j

        if i == len(prices) - 1:
            res += 1

        return res
        