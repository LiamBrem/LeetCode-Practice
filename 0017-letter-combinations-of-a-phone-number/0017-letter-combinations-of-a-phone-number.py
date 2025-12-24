class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def getLetters(num: int) -> list[str]: # assumes 2 <= num <= 9
            if 2 <= num <= 6:
                start = ord('a') + ((num - 2) * 3)
                return [chr(start), chr(start + 1), chr(start + 2)]
            elif num == 8:
                return ["t", "u", "v"]
            elif num == 7:
                return ["p", "q", "r", "s"]
            else:
                return ["w", "x", "y", "z"]

        res = []

        def dfs(i, curr):
            if i >= len(digits):
                res.append(curr)
                return

            letters = getLetters(int(digits[i]))
            for letter in letters:
                dfs(i + 1, curr + letter)
            
        dfs(0, "")
        return res 