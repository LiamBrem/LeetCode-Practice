class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0

        while len(nums) > 1:
            minVal, minIndex = float('inf'), 1
            isDecreasing = False 
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    isDecreasing = True
                
                if nums[i] + nums[i + 1] < minVal:
                    minVal = nums[i] + nums[i + 1]
                    minIndex = i

            if not isDecreasing:
                return res

            nums[minIndex] = minVal
            nums = nums[:minIndex + 1] + nums[minIndex + 2:]
            res += 1

        return res
        