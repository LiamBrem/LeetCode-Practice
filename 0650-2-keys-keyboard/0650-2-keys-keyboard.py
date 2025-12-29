"""
[0, 2, 3, 4, 5, 5, 7, 6, 6, 10, 11, 12]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

AAAAAAAAAA
"""
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        def factors(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return (i, num // i)

            return (1, num)


        for i in range(3, len(dp)):
            x, y = factors(i)
            if x == 1:
                dp[i] = i
            else:
                dp[i] = dp[x] + dp[y] 

        return dp[-1]
            