class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        configuration = []
        board = [['.']*n for _ in range(n)]

        def safe(row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1

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