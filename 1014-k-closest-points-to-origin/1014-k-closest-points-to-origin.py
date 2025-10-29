class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, y1):
            inside = x1 ** 2 + y1 ** 2
            return abs(inside)

        distances = [distance(point[0], point[1]) for point in points]

        zipped = list(zip(distances, points))

        heapq.heapify(zipped)

        res = []

        for i in range(k):
            z = heapq.heappop(zipped)
            point = z[1]
            res.append(point)

        return res

        