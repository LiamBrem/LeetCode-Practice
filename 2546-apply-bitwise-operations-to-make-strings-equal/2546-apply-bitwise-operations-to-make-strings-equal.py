"""
replace 1 with or
replace other with xor

1, 1 -> 1, 0

0, 0 -> 0, 0

1, 0 -> 1, 1
"""
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if ("1" not in s or "1" not in target) and not ("1" not in s and "1" not in target):
            return False
        else:
            return True

        