"""
Balanced:
maxVal <= k * minVal

can remove any element w/o making empty
return minimum number to make balanced

[1, 2, 6, 9] k = 3
[1, 1, 1, 1, 1, 1, 1, 2, 9] k = 3

[1, 2, 5] k = 2

[1, 23, 34] k = 2

[5, 11, 20]
"""

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        res = 0
        for l in range(len(nums)):
            while r + 1 < len(nums) and nums[l] * k >= nums[r + 1]:
                r += 1
            res = max(res, r - l + 1) # maximum window where max < min * k

        return len(nums) - res # extra space



        