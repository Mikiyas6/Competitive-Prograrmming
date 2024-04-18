class Solution:
    def totalNQueens(self, n: int) -> int:

        board = [[False]*n for _ in range(n)]

        def is_safe(board,row,col):

            diagonally_right = min(row,n-col-1)
            for i in range(1,diagonally_right+1):
                if board[row-i][col+i]:
                    return False
            diagonally_left = min(row,col)
            for i in range(1,diagonally_left+1):
                if board[row-i][col-i]:
                    return False
            up = row
            for i in range(1,up+1):
                if board[row-i][col]:
                    return False

            return True

        def fun(board,row):

            if row == n:

                return 1
            
            counter = 0

            for col in range(n):

                if is_safe(board,row,col):

                    board[row][col] = True
                    counter += fun(board,row+1)
                    board[row][col] = False
            
            return counter
        
        return fun(board,0)