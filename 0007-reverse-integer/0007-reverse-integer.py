class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x >= 0:
            res = int(s[::-1]) 
        else:
            res = int(s[1:][::-1]) * -1

        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0

        return res


        
