class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if num > 0:
                res[i] = nums[(i + num) % len(nums)]
            elif num < 0:
                res[i] = nums[i-abs(num) % len(nums)]
            else:
                res[i] = num


        return res



        
        