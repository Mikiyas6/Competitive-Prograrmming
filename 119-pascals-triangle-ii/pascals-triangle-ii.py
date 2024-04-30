class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        n = rowIndex

        board = [[0]*(n+1) for _ in range(n+1)]

        def store(board,row,col,value):
            board[row][col] = value
            return

        def fun(row,col):

            if row == n+1:
                return

            if row == col:
                value = 1
                store(board,row,col,value)
                fun(row+1,0)
                return
            
            if col == 0:
                value = 1
                store(board,row,col,value)
                fun(row,col+1)
                return
            
            value = board[row-1][col-1] + board[row-1][col]
            store(board,row,col,value)
            fun(row,col+1)
            return
        
        fun(0,0)
        return board[-1]
        

            
