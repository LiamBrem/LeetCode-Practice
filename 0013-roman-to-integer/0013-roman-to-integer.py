class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        level = "I"
        res = 0
        for char in s[::-1]:
            if m[char] > m[level]:
                level = char
                res += m[char]
            elif m[char] == m[level]:
                res += m[char]
            else:
                res -= m[char]

        return res

