"""
[1, 7, 9, 8, 2] k = 2
---

[12,16,19,19,8,1,19,13,9], k = 3
[12, 16, 19], [1, 19]


[19, 1], [19, 9]

"""


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # 0 -> nothing 1 -> normal 2 -> selling


        memo = [[[None] * 3 for _ in range(k + 1)] for _ in range(len(prices)+ 1)]
        def dfs(i, state, transactions):
            if i >= len(prices):
                if state != 0:
                    return -float('inf')
                else:
                    return 0

            if transactions >= k:
                return 0

            if memo[i][transactions][state] is not None:
                return memo[i][transactions][state]

            # do nothing
            ans = dfs(i + 1, state, transactions)

            if state == 0:
                # can buy, sell, do nothing
                # buy
                ans = max(ans, dfs(i + 1, 1, transactions) - prices[i])

                # sell
                ans = max(ans, dfs(i + 1, 2, transactions) + prices[i])

            elif state == 1:
                # can sell, do nothing
                ans = max(ans, dfs(i + 1, 0, transactions + 1) + prices[i])


            elif state == 2:
                # can buy, do nothing
                ans = max(ans, dfs(i + 1, 0, transactions + 1) - prices[i])
            
            memo[i][transactions][state] = ans
            return ans

        return dfs(0, 0, 0)
            
        
        