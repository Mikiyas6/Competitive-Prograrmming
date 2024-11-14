class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        configuration = []
        board = [['.']*n for _ in range(n)]

        def safe(row,col):

            for i in range(row+1):
                if board[i][col] == 'Q':
                    return False
            
            for i in range(1,n-col):
                if board[row-i][col+i] == 'Q':
                    return False
            
            for i in range(1,col+1):
                if board[row-i][col-i] == 'Q':
                    return False
            
            return True

        def backtrack(row,board):
            if row == n:
                configuration.append(["".join(row) for row in board[:]])
                return
            for col in range(n):
                if safe(row,col):
                    board[row][col] = "Q"
                    backtrack(row+1,board)
                    board[row][col] = '.'

        backtrack(0,board)
        
        return configuration