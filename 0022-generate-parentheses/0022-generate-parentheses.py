"""
())(

)()
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def dfs(o, c, s):
            print(s)
            if len(s) >= n * 2:
                self.res.append(s)
                return
           
            if len(s) == 0:
                dfs(o + 1, c, "(") 

            elif o >= n:
                dfs(o, c + 1, s + ")")

            else:
                dfs(o + 1, c, s + "(")
                if o > 0 and c < o:
                    dfs(o, c + 1, s + ")")

            
        dfs(0, 0, "")
        return self.res
