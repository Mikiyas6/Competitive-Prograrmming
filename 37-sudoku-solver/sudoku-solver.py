class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = 9

        def inbound(row, col):
            return 0 <= row < 9 and 0 <= col < 9

        def inboundAndSafe(row, col, value, board):
            if not inbound(row, col):
                return False
            value = str(value)
            for i in range(9):
                if board[row][i] == value or board[i][col] == value:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == value:
                    return False
            return True

        def sudoku(row, col, board):
            if row == 9:
                return True
            
            if col == 9:
                return sudoku(row + 1, 0, board)
            
            if board[row][col] != '.':
                return sudoku(row, col + 1, board)
            
            for value in range(1, 10):
                if inboundAndSafe(row, col, value, board):
                    board[row][col] = str(value)
                    if sudoku(row, col + 1, board):
                        return True
                    board[row][col] = '.'
            
            return False

        sudoku(0, 0, board)