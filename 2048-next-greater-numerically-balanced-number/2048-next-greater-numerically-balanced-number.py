from itertools import permutations
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        balancedNums = []
        seen = set()
        bases = [
            {"1":1},
            {"2":2},
            {"1":1,"2":2},
            {"3":3},
            {"1":1,"3":3},
            {"4":4},
            {"1":1,"4":4},
            {"2":2,"3":3},
            {"5":5},
            {"1":1,"2":2,"3":3},
            {"1":1,"5":5},
            {"2":2,"4":4},
            {"6":6},
            {"1":1,"2":2,"4":4},
            {"1":1,"6":6},
            {"2":2,"5":5},
            {"3":3,"4":4},
            {"7":7},
            {"1":1,"2":2,"5":5},
        ]


        def dfs(counts, path):
            if sum(counts.values()) == 0:
                balancedNums.append(int(path))
                return

            for d in list(counts.keys()):
                if counts[d] > 0:
                    counts[d] -= 1
                    dfs(counts, path + d)
                    counts[d] += 1
               
            
        for base in bases:
            dfs(base, "")

        balancedNums.sort()

        l, r = 0, len(balancedNums) - 1

        while l < r:
            mid = (l + r) // 2
            if balancedNums[mid] > n:
                r = mid

            elif balancedNums[mid] <= n:
                l = mid + 1


        return balancedNums[l]
    