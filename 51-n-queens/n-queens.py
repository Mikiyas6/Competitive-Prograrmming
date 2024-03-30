class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        configurations = []

        def store(board):

            new_board = []

            for row in board:

                string = ""

                for column in row:

                    if column == True:

                        string += "Q"
                    
                    else:

                        string += "."
            
                new_board.append(string)

            configurations.append(new_board)
        
        def is_safe(board,row,col):

            # Checking upwards

            journey = row

            for i in range(1,journey+1):

                if board[row-i][col]:

                    return False

            # Checking Left Diagonal
            
            journey = min(row,col)

            for i in range(1,journey+1):

                if board[row-i][col-i]:

                    return False
            
            # Checking right Diagonal
            
            journey = n - col - 1

            for i in range(1,journey+1):

                if board[row-i][col+i]:

                    return False
            
            return True
            
        def N_Queens(board,row):

            if row == n:
                store(board)

                return
            
            for i in range(n):

                if is_safe(board,row,i):

                    board[row][i] = True

                    N_Queens(board,row+1)

                    board[row][i] = False
            
            return 
        
        board = [[False]*n for _ in range(n)]
        
        N_Queens(board,0)

        return configurations