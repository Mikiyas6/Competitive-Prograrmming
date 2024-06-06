class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        configurations = []
        board = [['.']*n for _ in range(n)]

        def store(board):

            nonlocal configurations
            
            boards = []
            for row in board:
                boards.append(''.join(row))

            configurations.append(boards)
                
        def inbound(row,col):
            
            return 0 <= row and row < n and 0 <= col and col < n

        def inboundAndSafe(row,col):

            if not inbound(row,col):
                return False
            
            left = min(row,col)
            right = min(row,(n-col-1))
            up = row
            
            for i in range(1,left+1):
                if board[row-i][col-i] == "Q":
                    return False
            
            for i in range(1,right+1):
                if board[row-i][col+i] == "Q":
                    return False
            
            for i in range(1,up+1):
                if board[row-i][col] == "Q":
                    return False
            
            return True
            
        def NQueens(row,board):
            
            if row == n:
                store([row[:] for row in board])
            
            for col in range(n):
                
                if inboundAndSafe(row,col):
                    board[row][col] = 'Q'
                    NQueens(row+1,board)
                    board[row][col] = '.'
            
            return

        NQueens(0,board)

        return configurations