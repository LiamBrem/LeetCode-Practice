class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1, m2 = float('-inf'), float('-inf')

        for num in nums:
            if num >= m1:
                m2 = m1
                m1 = num
            elif num <= m1 and num >= m2:
                m2 = num

        print(m1, m2)
        return (m1 - 1) * (m2 - 1)
        