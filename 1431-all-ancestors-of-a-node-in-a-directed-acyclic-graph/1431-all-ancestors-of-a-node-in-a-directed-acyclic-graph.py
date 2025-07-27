from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for f, t in edges:
            adj[f].append(t)

        ans = [[] for _ in range(n)]

        def dfs(x, curr):
            for ch in adj[curr]:
                if not ans[ch] or ans[ch][-1] != x:
                    ans[ch].append(x)
                    dfs(x, ch)


        for i in range(n):
            dfs(i, i)
        return ans

        