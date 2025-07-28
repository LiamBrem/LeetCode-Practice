import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            dif = -abs(s1 - s2)
            if dif != 0:
                heapq.heappush(stones, dif)

        return 0 if len(stones) == 0 else abs(stones[0])
            
        
        