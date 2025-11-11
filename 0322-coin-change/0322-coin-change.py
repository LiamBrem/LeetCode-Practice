class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # amount[i] = min number of coins to reach i
        dp = [amount + 1] * (amount + 1)

        for i in range(1, len(dp)):
            currMin = amount + 1
            for coin in coins:
                # subtract from total
                leftOver = i - coin
                if leftOver == 0:
                    curAmount = 1
                elif leftOver > 0:
                    curAmount = 1 + dp[leftOver] if dp[leftOver] != amount + 1 else amount + 1
                else:
                    curAmount = amount + 1
                    
                currMin = min(currMin, curAmount)

            dp[i] = currMin

        return dp[-1] if dp[-1] != amount + 1 else -1
