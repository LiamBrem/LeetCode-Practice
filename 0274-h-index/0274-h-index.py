class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i, amount in enumerate(citations):
            if amount >= n - i:
                return n - i

        return 0


        # 6 5 3 1 0