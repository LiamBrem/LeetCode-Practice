class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (m)] * n


        dp[0][0] = 1
        rows, cols = len(dp), len(dp[0])

        for row in range(rows):
            for col in range(cols): 
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]




        return dp[-1][-1]