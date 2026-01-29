class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        adj = defaultdict(list)
        costs = {}

        for i in range(len(changed)):
            frm, to, singleCost = original[i], changed[i], cost[i]
            adj[frm].append(to)
            if (frm, to) in costs:
                costs[(frm, to)] = min(costs[(frm, to)], singleCost)
            else:
                costs[(frm, to)] = singleCost

        def minCost(s, t):
            q = [(0, s)]
            visited = set()
            distances = {}

            while q:
                currDist, currNode = heapq.heappop(q)
            
                if currNode == t:
                    return currDist 
                    
                if currNode in visited:
                    continue

                visited.add(currNode)
                distances[currNode] = currDist

                for neighbor in adj[currNode]:
                    if neighbor not in visited:
                        weight = costs[(currNode, neighbor)]
                        distance = currDist + weight
                        heapq.heappush(q, (distance, neighbor))

            return distances[t] if t in distances else -1
                
        res = 0
        seen = {}

        for i in range(len(source)):
            s, t = source[i], target[i]
            if s != t:
                if (s, t) in seen:
                    res += seen[(s, t)]

                else:   
                    c = minCost(s, t)
                    if c == -1:
                        return -1 
                    
                    seen[(s, t)] = c
                    res += c

        return res
        