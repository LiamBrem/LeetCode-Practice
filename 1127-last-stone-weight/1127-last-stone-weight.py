import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            diff = abs(stone1) - abs(stone2)

            if diff != 0:
                if diff > 0: # stone1
                    heapq.heappush(stones, -diff)
                else: #stone2
                    heapq.heappush(stones, diff)

        if len(stones) == 1:
            return abs(stones[0])
        else:
            return 0
            
        
        