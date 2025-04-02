class Solution:
    def maxScore(self, s: str) -> int:
        oneCount = s.count('1')
        zeroCount = 0
        m = 0
        
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeroCount += 1
            else:
                oneCount -= 1
            m = max(m, zeroCount + oneCount)
        
        return m
