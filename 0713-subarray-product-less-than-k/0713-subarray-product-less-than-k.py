class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        l = 0
        currProd = 1
        res = 0

        for r in range(len(nums)):  
            currProd *= nums[r]

            while currProd >= k and l <= r:
                currProd //= nums[l]
                l += 1

            length = r - l
            res += length + 1

        return res
            

            
    
