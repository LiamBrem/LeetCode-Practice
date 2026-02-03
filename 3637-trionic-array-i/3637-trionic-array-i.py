class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # 0 = increasing, 1 = decreasing, 2 = increasing
        if len(nums) <= 3:
            return False 

        count = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return False

            if i == 0 and nums[i + 1] < nums[i]:
                return False

            if count == 0:
                if nums[i] > nums[i + 1]:
                    count += 1
            
            elif count == 1:
                if nums[i] < nums[i + 1]:
                    count += 1


            elif count == 2:
                if nums[i] >= nums[i + 1]:
                    return False

        return True if count == 2 else False


        