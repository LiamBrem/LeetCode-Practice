class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        def dfs(level, i):
            if level >= len(triangle):
                return 0

            newLevel = level + 1
            return triangle[level][i] + min(dfs(newLevel, i), dfs(newLevel, i + 1))

        return dfs(0, 0)
        
        '''


        for i in range(len(triangle) -2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]

