'''
input: array nums (either 1 or 0)
    - int k

output: int 

notes: 
    - max num of consecutive 1s if you can flip at most k 0s
    - i.e. can turn k 0s into 1s


[1, 1, 1, 

0, 0, 1, 1, 1, 1, 0], 0

[1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 3


[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 

1


'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        remainingZeroes = k
        maxSize = 0

        r = l = 0

        while r < len(nums):
            if nums[r] == 0:
                remainingZeroes -= 1
      
                while remainingZeroes < 0:
                    if nums[l] == 0:
                        remainingZeroes += 1
                    l += 1

            
            maxSize = max(maxSize, (r - l + 1))
            r += 1

            
        return maxSize