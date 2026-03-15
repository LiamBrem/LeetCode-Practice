class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1 and not edges:
            return 0

        stronger = set()
        seen = set()
        for i, j in edges:
            stronger.add(i)
            stronger.add(j)
            seen.add(i)
            seen.add(j)

        for _, j in edges:
            if j in stronger:
                stronger.remove(j)

        if len(stronger) != 1 or len(seen) != n:
            return -1
        else:
            return stronger.pop()
        