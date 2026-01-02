from collections import defaultdict
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
            if d[num] >= n:
                return num        