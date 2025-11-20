'''
input: 
    - strings s & t (anagrams)
    - int k

- split s into k equal sized substrings
    - s.length always divisible by k

- rearrange + concat to form new string matching t

output: 
    - true if possible
    - false otherwise

nngg, gnng

nngg, nngg
'''

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        seen = defaultdict(int) 
        size = len(s) // k 
        for i in range(0, len(s), size):
            seen[s[i:i + size]] += 1

        for i in range(0, len(s), size):
            if t[i: i + size] in seen and seen[t[i: i + size]] != 0:
                seen[t[i: i + size]] -= 1
            else:
                return False 


        return True
