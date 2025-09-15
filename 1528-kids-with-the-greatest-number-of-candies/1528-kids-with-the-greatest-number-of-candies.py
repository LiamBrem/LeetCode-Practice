class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatestAmount = max(candies)

        for candy in candies:
            if candy + extraCandies >= greatestAmount:
                result.append(True)
            else:
                result.append(False)

        return result


        