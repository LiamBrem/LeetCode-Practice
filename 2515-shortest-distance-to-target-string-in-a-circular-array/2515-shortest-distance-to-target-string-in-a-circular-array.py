class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        l = r = startIndex
        count = 0
        flag = True


        while flag or l != r:
            flag = False
            
            if words[l] == target or words[r] == target:
                break
            
            r += 1
            r %= len(words)
            l -= 1
            l %= len(words)

            count += 1

        if words[l] == target or words[r] == target:
            return count
        
        return -1
        