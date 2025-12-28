"""
AABABBA
k = 1
freq: {a: 1, b: 2}
currLen: 3
maxFreq: 2
res: 4
"""

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        i = 0
        freq = defaultdict(int)

        for j in range(len(s)):
            # expand
            freq[s[j]] += 1
            currLen = j - i + 1
            maxFreq = max(freq.values())

            while currLen - maxFreq > k:
                freq[s[i]] -= 1
                maxFreq = max(freq.values())
                i += 1
                currLen -= 1

            res = max(res, currLen)

        return res     