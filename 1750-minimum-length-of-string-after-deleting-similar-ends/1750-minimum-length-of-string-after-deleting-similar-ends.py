"""
cabaabac


"""
class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) >= 2 and s[0] == s[-1]:
            i, j = 0, len(s) - 1
            while i < len(s) and s[i] == s[0]:
                i += 1
            while j >= 0 and s[j] == s[0]:
                j -= 1

            s = s[i:j + 1]

        return len(s)
        