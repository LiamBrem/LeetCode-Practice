'''
input: gifts - gifts[i] = # of gifts in pile i
output: number of gifts remaining after k seconds


notes:
    - each second:
        - choose pile w/ max gifts (if multiple, any)
        - reduce to floor(sqrt(gifts))



'''


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            largestGift = heapq.heappop(gifts)
            gift = floor(abs(largestGift) ** 0.5)
            heapq.heappush(gifts, -gift)

        return sum([-gift for gift in gifts])
        