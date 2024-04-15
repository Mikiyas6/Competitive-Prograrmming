class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        configurations = []

        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
                if col-row+i >= 0 and board[i][col-row+i] == "Q":
                    return False
                if col+row-i < n and board[i][col+row-i] == "Q":
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
                    fun(board, row + 1)
                    board[row][col] = "."

        fun(board, 0)

        return configurations
