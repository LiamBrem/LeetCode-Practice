class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9

        def isValidRows(board):
            for row in range(size):
                seen = set()
                for col in range(size):
                    if board[row][col] != "." and board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])

            return True


        def isValidCols(board):
            for col in range(size):
                seen = set()
                for row in range(size):
                    if board[row][col] != "." and board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])

            return True


        def isValidSquares(board):
            for i in range(3):
                for j in range(3):
                    startRow = i * 3
                    startCol = j * 3
                    seen = set()

                    for r in range(startRow, startRow + 3):
                        for c in range(startCol, startCol + 3):
                            if board[r][c] != "." and board[r][c] in seen:
                                return False
                            else:
                                seen.add(board[r][c])

            return True




        return isValidRows(board) and isValidCols(board) and isValidSquares(board)