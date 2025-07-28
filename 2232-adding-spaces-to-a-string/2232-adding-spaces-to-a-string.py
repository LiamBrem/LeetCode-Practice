class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        result = ""
        spaces = spaces[::-1]

        while i < len(s):
            if len(spaces) > 0 and i == spaces[-1]:
                result += " "
                spaces.pop()
            else:
                result += s[i]
                i += 1


        return result
        