class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr, prev, ans = 1, 0, 0

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1

        ans += min(prev, curr)

        return ans 

