class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        smallestVal = float('inf')

        for i in range(len(nums)):
            if nums[i] == target:
                smallestVal = min(smallestVal, abs(i - start))

        return smallestVal
        