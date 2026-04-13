class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        res = [0] * (len(nums) + 2)

        for i, num in enumerate(nums):
            pos = i + 2

            res[pos] = max(num + res[pos - 2], res[pos - 1])

        return res[-1]
