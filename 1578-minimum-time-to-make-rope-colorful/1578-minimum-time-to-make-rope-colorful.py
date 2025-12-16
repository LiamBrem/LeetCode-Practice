class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        p1, p2 = 0, 1

        res = 0

        while p2 < len(neededTime):
            if colors[p1] == colors[p2]:
                res += (min(neededTime[p1], neededTime[p2]))

                if neededTime[p1] < neededTime[p2]:
                    p1 = p2
            
            else:
                p1 = p2

            p2 += 1

        
        return res