class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        counter = Counter(nums)
        for num in counter.keys():
            if counter[num] >= n:
                return num

        return -1
        