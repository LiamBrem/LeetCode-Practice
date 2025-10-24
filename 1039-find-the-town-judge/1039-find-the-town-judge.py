"""
input: n = (int) people, trust = (2d array) 
trust[i] = [a, b] -> ai trusts bi

output: 
    - label of town judge
    - if doesn't exist: -1

notes:
    - town judge doesn't trust anyone
"""
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1 
        
        trustCount = defaultdict(int)
        trustedBy = defaultdict(int)
        possibleJudges = set(range(1, n + 1))
        
        for a, b in trust:
            if a in possibleJudges:
                possibleJudges.remove(a)
                
            trustCount[a] += 1
            trustedBy[b] += 1

        for candidate in possibleJudges:
            if trustedBy[candidate] == n - 1:
                return candidate
        
        return -1

        