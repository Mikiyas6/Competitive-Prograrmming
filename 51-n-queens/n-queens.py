class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."]*n for _ in range(n)]

        configurations = []

        def is_safe(board,row,col):
            diagonal_right = min(row,n-col-1)
            for i in range(1,diagonal_right+1):
                if board[row-i][col+i] == "Q":
                    return False
            
            diagonal_left = min(row,col)
            for i in range(1,diagonal_left+1):
                if board[row-i][col-i] == "Q":
                    return False

            for i in range(1, row + 1):
                if board[row-i][col] == "Q":
                    return False
                
            return True
        
        def fun(board, row):
            if row == n:
                # Append a copy of the board, not the board itself
                configurations.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = "Q"
                    fun([row[:] for row in board], row + 1)  # Create a deep copy of the board
                    board[row][col] = "."

        fun(board, 0)

        return configurations
        
        