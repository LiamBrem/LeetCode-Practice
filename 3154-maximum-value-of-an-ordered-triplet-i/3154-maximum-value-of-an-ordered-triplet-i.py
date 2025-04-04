class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxTrip = maxElem = maxDiff = 0
        for num in nums:
            maxTrip = max(maxTrip, maxDiff * num)
            maxDiff = max(maxDiff, maxElem - num)
            maxElem = max(maxElem, num)
        return maxTrip