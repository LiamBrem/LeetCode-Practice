import math

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0

        prefixes = set()
        for val in arr1:
            while val not in prefixes and val > 0:
                prefixes.add(val)
                val //= 10

        for val in arr2:
            while val not in prefixes and val > 0:
                val //= 10

            if val > 0:
                res = max(res, int(math.log10(val)) + 1)

        return res

