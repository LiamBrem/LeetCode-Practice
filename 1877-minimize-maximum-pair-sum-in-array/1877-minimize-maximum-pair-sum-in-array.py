"""
2, 3, 4, 4, 5, 6
1, 19, 19, 19, 19, 20

[4,1,5,1,2,5,1,5,5,4]
1, 1, 1, 3, 4, 4, 5, 5, 5, 5
"""
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        maxSum = float('-inf')

        for i in range(len(nums) // 2):
            maxSum = max(maxSum, nums[i] + nums[-(i + 1)])

        return maxSum