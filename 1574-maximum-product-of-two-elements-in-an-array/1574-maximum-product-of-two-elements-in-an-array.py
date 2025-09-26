import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        print(num1, num2)
        return ((-num1) - 1) * ((-num2) - 1)
        