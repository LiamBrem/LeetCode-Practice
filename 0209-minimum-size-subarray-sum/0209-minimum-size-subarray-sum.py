class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLen = float('inf')

        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                minLen = min((r - l + 1), minLen)
                curr -= nums[l]
                l += 1

        return minLen if minLen != float('inf') else 0

         
        