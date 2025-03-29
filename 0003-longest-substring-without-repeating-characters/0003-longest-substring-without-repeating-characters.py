class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0

        currentChars = set()
        longest = 0
        slow = 0

        for fast in range(len(s)):

            while s[fast] in currentChars:
                currentChars.remove(s[slow])
                slow += 1

            difference = fast - slow + 1
            if difference + 1 > longest:
                longest = difference
                
            currentChars.add(s[fast])
            fast += 1

        return longest


            
            
        