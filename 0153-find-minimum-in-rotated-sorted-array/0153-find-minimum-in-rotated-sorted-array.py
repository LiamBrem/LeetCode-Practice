class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            nextPos = (mid + 1) % len(nums)
            prevPos = (mid - 1) % len(nums)

            if nums[mid] < nums[nextPos] and nums[nextPos] < nums[prevPos]:
                return nums[mid]

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return min(nums[l], nums[r])