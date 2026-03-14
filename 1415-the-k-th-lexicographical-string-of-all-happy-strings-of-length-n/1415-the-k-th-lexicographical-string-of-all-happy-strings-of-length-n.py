class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.res = []

        def dfs(curr):
            if len(curr) == n:
                self.res.append(curr)

            elif len(curr) > n:
                return

            for letter in ['a', 'b', 'c']:
                if not curr or curr[-1] != letter:
                    dfs(curr + letter)

        dfs("")


        return "" if len(self.res) < k else self.res[k - 1]
        