"""
())(

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        maxLen = n * 2

        def dfs(openCount, completedCount, curr):
            if len(curr) >= maxLen:
                res.append(curr)
                return

            if len(curr) == 0:
                dfs(1, 0, "(")

            elif openCount >= n:
                dfs(openCount, completedCount + 1, curr + ")")

            else:
                dfs(openCount + 1, completedCount, curr + "(")
                if openCount > completedCount:
                    dfs(openCount, completedCount + 1, curr + ")")

        dfs(0, 0, "")

        return res