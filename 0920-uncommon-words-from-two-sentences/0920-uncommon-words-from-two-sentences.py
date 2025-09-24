from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = defaultdict(int)

        for word in s1.split(" "):
            hashmap[word] += 1
        
        for word in s2.split(" "):
            hashmap[word] += 1

        res = []

        for word in hashmap:
            if hashmap[word] == 1:
                res.append(word)

        return res
            

        
    
