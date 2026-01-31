class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) -1 
        if letters[-1] <= target or letters[0] > target:
            return letters[0]

        while l < r:
            mid = (l + r) // 2
            print(l, r, mid, letters[mid])
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid

        return letters[l]

        