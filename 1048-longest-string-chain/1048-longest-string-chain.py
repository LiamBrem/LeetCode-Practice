class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words = sorted(words, key=lambda x: len(x))

        for word in words:
            preds = []
            if len(word) > 1:
                for i in range(len(word)):
                    newWord = word[:i] + word[i + 1:]

                    if newWord in dp:
                        preds.append(dp[newWord])

            if preds:
                dp[word] = max(preds) + 1
            else:
                dp[word] = 1

        return max(dp.values()) 
        