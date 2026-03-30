class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        unique = set(candyType)
        uniqueCount = len(unique)

        if uniqueCount < n // 2:
            return uniqueCount
        else:
            return n // 2


        