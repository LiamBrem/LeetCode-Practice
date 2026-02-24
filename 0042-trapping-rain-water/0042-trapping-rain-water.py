class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        res = 0

        for h in height:
            while s and h > s[-1]: # go back 
                temp = []
                low = s[-1]
                while s and s[-1] <= low:
                    temp.append(s.pop())

                if not s:
                    s = temp[::-1]
                    s.append(h)
                    break
                
                else:
                    fill = min(h, s[-1])
                    while temp:
                        res += fill - temp.pop()
                        s.append(fill)

            s.append(h)

        return res


        