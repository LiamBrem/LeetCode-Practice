class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        second = third = float('inf')

        for i in range(1, len(nums)):
            num = nums[i]
            if num < second:
                third = second
                second = num
            elif num < third:
                third = num

        return first + second + third
                

        