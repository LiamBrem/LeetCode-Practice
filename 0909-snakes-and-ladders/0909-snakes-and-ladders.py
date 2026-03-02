class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        direction = 1 # * by -1 each iter

        q = deque()
        rows, cols = len(board), len(board[0])
        N = rows ** 2

        q.append((1, 0)) # row, col, num, moves

        def calculatePosition(num):
            n = rows  
            row_from_bottom = (num - 1) // n
            col = (num - 1) % n
        
            row = n - 1 - row_from_bottom
        
            if row_from_bottom % 2 == 1:
                col = n - 1 - col
    
            return row, col


        res = float('inf')
        seen = set()

        while q: 
            num, moves = q.popleft()

            if num == N:
                res = min(res, moves)
                continue

            if (num) in seen:
                continue

            seen.add(num)

            for i in range(num + 1, min(N, num + 6) + 1):
                nextNum = i
                nRow, nCol = calculatePosition(nextNum)
                if board[nRow][nCol] != -1:
                    nextNum = board[nRow][nCol]

                q.append((nextNum, moves + 1))


        return res if res != float('inf') else -1

