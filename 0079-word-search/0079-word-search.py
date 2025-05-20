class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if word[index] != board[i][j]:
                return False

            temp = board[i][j]
            board[i][j] = ''

            if dfs(i+1, j, index+1) or dfs(i-1, j, index + 1) or dfs(i, j+1, index+1) or dfs(i, j-1, index+1):
                return True

            board[i][j] = temp
            return False

            

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False
