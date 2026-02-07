"""
minimum number of deletions to achieve
all "a" -> all "b"
"aaaabbbbbb"

could find point in arr where prev half is mostly A and second half is mostly B


abababbbaabbbbb

"aababbab"
[3, 2, 2, 1, 1, 1, 0, 0]
[4, 4, 3, 3, 2, 1, 1, 0]

bbaaaaabb

A = 5


"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        countA = 0 # A to right of pointer
        countB = 0 # B to left of pointer

        for char in s:
            if char == "a":
                countA += 1

        res = float('inf')
        for char in s:
            if char == "a":
                countA -= 1
            res = min(res, countA + countB)
            if char == "b":
                countB += 1

        return res