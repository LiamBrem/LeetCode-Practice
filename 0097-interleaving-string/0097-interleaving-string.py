"""
n = number of substrings of s
m = number of substrings of t

n and m can't differ by more than 1
the number of substrings from n and m must differ by no more than 1

"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False


        @lru_cache(None)
        def dfs(i, s1i, s2i):
            if i >= len(s3):
                return True

            res = False

            if s1i < len(s1) and s1[s1i] == s3[i]:
                res |= dfs(i + 1, s1i + 1, s2i)
            if s2i < len(s2) and s2[s2i] == s3[i]:
                res |= dfs(i + 1, s1i, s2i + 1)
            return res 
            

        return dfs(0, 0, 0)