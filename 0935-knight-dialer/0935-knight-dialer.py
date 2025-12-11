class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        validNums = {1: [8, 6], 2: [7, 9], 3: [8, 4], 4:[0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6]}

        @lru_cache(None)
        def dfs(num, count):
            if count >= n:
                return 1

            total = 0
            for number in validNums[num]:
                total += dfs(number, count + 1) 

            return total

        total = 0
        for i in range(10):
            if i != 5:
                total += dfs(i, 1) 

        return total%(10**9+7) 