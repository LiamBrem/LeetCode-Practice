"""
Brute force (O(N^2))
    - loop through each person
    - for each person, loop through each prson to the right, keeping track of max
    - if the persons height to the right is greater than max, increment and continue

res = [0] * len(heights)
    for i, height in enumerate(heights):
        largest = 0
        for j in range(i + 1, len(heights)):
            neighborHeight = heights[j]
            if largest < height and neighborHeight > largest:
                largest = neighborHeight
                res[i] += 1
    return res

Faster:
    - stack, only in increasing order going to the right

"""
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        s = []
        res = [0] * len(heights)

        for i in range(len(heights) -1, -1, -1): 
            height = heights[i]

            while s and height > s[-1]:
                s.pop()
                res[i] += 1

            if s and s[-1] > height:
                res[i] += 1

            if i != len(heights) - 1 and res[i] == 0:
                res[i] = 1

            s.append(height)

        return res

        