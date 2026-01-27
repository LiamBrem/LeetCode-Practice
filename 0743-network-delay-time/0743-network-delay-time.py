class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[k - 1] = 0
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        q = [(0, k)]

        while q: # while there are still unvisited nodes
            currDist, currNode = heapq.heappop(q)

            if currDist > distances[currNode - 1]:
                continue

            for neighbor, weight in adj[currNode]:
                distance = currDist + weight
                if distance < distances[neighbor - 1]:
                    distances[neighbor - 1] = distance
                    heapq.heappush(q, (distance, neighbor))

        return -1 if float('inf') in distances else max(distances)



            