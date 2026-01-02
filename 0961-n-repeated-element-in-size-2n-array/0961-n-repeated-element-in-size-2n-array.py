from collections import defaultdict
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        d = defaultdict(int)

        for num in nums:
            if d[num] + 1 >= n:
                return num

            d[num] += 1