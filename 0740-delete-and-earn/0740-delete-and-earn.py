from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0


        freq = Counter(nums)
        nums_sorted = sorted(freq.keys())

        dp = [0] * len(nums_sorted)

        for i, num in enumerate(nums_sorted):
            curr = num * freq[num]

            if i == 0:
                dp[i] = curr
            elif num == nums_sorted[i - 1] + 1:
                dp[i] = max(dp[i - 1], (dp[i - 2] if i > 1 else 0) + curr)
            else:
                dp[i] = dp[i-1] + curr


        return dp[-1] 
        