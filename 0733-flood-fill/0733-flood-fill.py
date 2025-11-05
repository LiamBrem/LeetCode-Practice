class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]
        q.append((sr, sc)) 
        seen = set()

        while len(q) > 0:
            r, c = q.popleft()
            seen.add((r, c))
            print(r, c)
            image[r][c] = color

            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if (0 <= newR < rows) and (0 <= newC < cols) and image[newR][newC] == original and (newR, newC) not in seen:

                    q.append((newR, newC))
    

        return image

            

        
        