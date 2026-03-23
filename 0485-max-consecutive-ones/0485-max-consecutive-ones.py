class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        most = 0

        while curr < len(nums):
            if nums[curr] == 0:
                curr += 1
                pass

            currCount = 1
            i = curr

            while i < len(nums) and nums[i] == 1:
                currCount += 1
                i += 1

            most = max(most, currCount)
            curr = i

        return most - 1
        