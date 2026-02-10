class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        length = 0

        for i in range(n):
            evens = set()
            odds = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])

                if len(odds) == len(evens):
                    length = max(length, j - i + 1)


        return length 