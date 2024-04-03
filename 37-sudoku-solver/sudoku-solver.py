class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = 9

        def is_safe(row, col, value):
            for i in range(n):
                if board[i][col] == value:
                    return False
                
            for i in range(n):
                if board[row][i] == value:
                    return False
            
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            if any(board[start_row + r][start_col + c] == value for r in range(3) for c in range(3)):
                return False
            
            return True

        def sudoku(row, col, board):
            if row == n: 
                return True
            
            if col == n:
                return sudoku(row + 1, 0, board)
                
            if board[row][col] == ".": 
                for value in range(1, 10):
                    if is_safe(row, col, str(value)): 
                        board[row][col] = str(value) 
                        if sudoku(row, col + 1, board):
                            return True
                board[row][col] = "."
            
            else:
                return sudoku(row, col + 1, board)

        sudoku(0, 0, board)