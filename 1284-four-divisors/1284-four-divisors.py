from functools import lru_cache


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        @lru_cache(maxsize=128)
        def getDivisors(num):
            divisors = set()
            for i in range(1, isqrt(num) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                if len(divisors) > 4:
                    return -1 
            return sum(divisors) if len(divisors) == 4 else -1

        res = 0

        for num in nums:
            divisors = getDivisors(num)
            if divisors != -1:
                res += divisors

        return res
