class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordList = set(wordDict)

        @lru_cache()
        def dfs(s):
            if s == "":
                return True

            res = False

            for i in range(len(s) + 1):
                if s[:i] in wordList:
                    foundAnyWords = True
                    res |= dfs(s[i:])

            return res


        return dfs(s)

        