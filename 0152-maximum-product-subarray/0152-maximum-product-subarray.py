class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = curMin = 1

        for num in nums:
            prevMax = curMax
            prevMin = curMin

            curMax = max(prevMax * num, prevMin * num, num)
            curMin = min(prevMax * num, prevMin * num, num)

            res = max(res, curMax)

        return res