class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        while len(nums) != len(s):
            count += 1
            if len(nums) > 3:
                nums = nums[3:]
            else:
                nums = []


            s = set(nums)

        return count