class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diffs = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        return sum([diff if diff > 0 else 0 for diff in diffs])