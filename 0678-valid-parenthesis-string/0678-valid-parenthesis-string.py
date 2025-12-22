class Solution:
    def checkValidString(self, s: str) -> bool:

        # count = number of "(" in stack
        @lru_cache(None)
        def dfs(i, count):
            if i >= len(s):
                return count == 0

            ans = False

            if s[i] == "(" or s[i] == "*":
                ans |= dfs(i + 1, count + 1)

            if s[i] == ")" or s[i] == "*":
                if count >= 1:
                    ans |= dfs(i + 1, count - 1)
                else:
                    ans|= False

            if s[i] == "*":
                ans |= dfs(i + 1, count) # "" 

            return ans

        return dfs(0, 0)
