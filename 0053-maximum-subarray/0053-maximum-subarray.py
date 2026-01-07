class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = -float('inf')

        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0

        return maxSum
