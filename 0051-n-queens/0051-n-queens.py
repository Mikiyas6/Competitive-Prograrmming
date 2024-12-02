class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        configuration = []
        def isSafe(row,col,board):
            if board[row][col] == "Q":
                return False
            # Up the Column
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            # Diagonal top-right
            for i in range(1,n-col):
                if board[row-i][col+i] == "Q":
                    return False
            # Diagonal top-left
            for i in range(1,min(row,col)+1):
                if board[row-i][col-i] == "Q":
                    return False
            return True
        def store(board):
            newBoard = ["".join(row[:]) for row in board]
            configuration.append(newBoard)
        def backtrack(row,board):
            if row == n:
                store(board[:])
                return
            for col in range(n):
                if isSafe(row,col,board):
                    board[row][col] = 'Q'
                    backtrack(row+1,board)
                    board[row][col] = '.'
        backtrack(0,board)
        return configuration