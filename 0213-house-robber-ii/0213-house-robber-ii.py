class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
            
        max1 = 0
        prev1 = nums[0]
        prev2 = 0 

        for i in range(2, len(nums)):
            temp = prev1
            prev1 = max(prev1, prev2 + nums[i-1])
            prev2 = temp

        max1 = prev1

        max2 = 0
        prev1 = nums[1]
        prev2 = 0 

        for i in range(3, len(nums) + 1):
            temp = prev1
            prev1 = max(prev1, prev2 + nums[i-1])
            prev2 = temp

        max2 = prev1

        return max(max1, max2)