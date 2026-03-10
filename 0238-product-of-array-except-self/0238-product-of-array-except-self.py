class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suf = [0] * len(nums)
        pref[0] = 1
        suf[-1] = 1

        for i in range(1, len(nums)):
            pref[i] = pref[i -1] * nums[i - 1]

        for i in range(len(nums) -2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        res = []
        for i in range(len(nums)):
            res.append(pref[i] * suf[i])

        return res