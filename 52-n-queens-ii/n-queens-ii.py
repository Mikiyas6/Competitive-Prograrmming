class Solution:
    def totalNQueens(self, n: int) -> int:

        board = [['.']*n for _ in range(n)]
        counter = 0

        def store():

            nonlocal counter
            
            counter += 1
                
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
                store()
            
            for col in range(n):
                
                if inboundAndSafe(row,col):
                    board[row][col] = 'Q'
                    NQueens(row+1,board)
                    board[row][col] = '.'
            
            return

        NQueens(0,board)

        return counter