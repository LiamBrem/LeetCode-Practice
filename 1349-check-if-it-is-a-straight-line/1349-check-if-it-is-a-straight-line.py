class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def slope(p1, p2):
            print(p1, p2)
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if x2 - x1 == 0:
                return float('inf')
            else:
                return (y2 - y1)/(x2 - x1)

        initialSlope = slope(coordinates[0], coordinates[1])

        for i in range(2, len(coordinates)):
            if slope(coordinates[i], coordinates[i-1]) != initialSlope:
                return False

        return True



        