class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        totalArea = 0
        lo, hi = float('inf'), float('-inf')
        for x, y, l in squares:
            totalArea += l * l
            lo = min(lo, y)
            hi = max(hi, y + l)
        
        target = totalArea / 2.0
        
        for i in range(48):
            mid = (lo + hi) / 2.0
            curr = 0

            for x, y, l in squares:
                yArea = max(0, min(l, mid - y))
                curr += l * yArea

            if curr < target:
                lo = mid
            else:
                hi = mid


        return mid


        

        
        