class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        originalColor = image[sr][sc]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        seen = set()

        def isValid(i, j):
            if i >= 0 and i < len(image) and j >= 0 and j < len(image[0]):
                return True


        def dfs(i, j):
            seen.add((i, j))

            if image[i][j] == originalColor:
                image[i][j] = color

                for direction in dirs:
                    newI = i + direction[0]
                    newJ = j + direction[1]

                    if (newI, newJ) not in seen and isValid(newI, newJ):
                        dfs(newI, newJ)

            else:
                return  


        dfs(sr, sc)
        return image 


        
        