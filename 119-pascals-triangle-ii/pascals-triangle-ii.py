class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        n = rowIndex + 1
        
        matrix = [[0]*n for _ in range(n)]

        def fun(matrix,row,col):

            if row == n:

                return matrix
            
            if row == col:

                matrix[row][col] = 1

                return fun(matrix,row+1,0)
            
            if col == 0:

                matrix[row][col] =  1

            else:

                matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col] 
            
            return fun(matrix,row,col + 1)
        
        return fun(matrix,0,0)[-1]

        # n = rowIndex + 1
        
        # matrix = [[0]*n for _ in range(n)]

        # for row in range(n):

        #     for col in range(row+1):

        #         if row == col or col == 0:

        #             matrix[row][col] = 1
                
        #         else:

        #             matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col]
        
        # return matrix[-1]