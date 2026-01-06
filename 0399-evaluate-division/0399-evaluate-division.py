"""
a / b = 1.5
b / c = 2.5

a / c = a/b * b/c 
c / b = 1 / b / c
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        m = defaultdict(list)

        for i, equation in enumerate(equations):
            numerator, denominator = equation[0], equation[1]
            m[numerator].append((denominator, values[i]))
            m[denominator].append((numerator, 1 / values[i]))

        def find(source, target):
            if source not in m or target not in m:
                return -1.0

            q = deque()
            q.append([source, 1.0])
            seen = set([source])

            while q:
                letter, val = q.popleft()

                if letter == target:
                    return val 

                for neighbor, weight in m[letter]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append((neighbor, weight * val))

            return -1.0
            
        return [find(source, target) for source, target in queries]
        
