class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        row_length = len(mat)
        col_length = len(mat[0])

        result = []

        up = True

        row, col = 0, 0

        while row < row_length and row >= 0 and col < col_length and col >= 0:

            if up:

                while row < row_length and row >= 0 and col < col_length and col >= 0:

                    result.append(mat[row][col])

                    row -= 1
                    col += 1

                if (row >= row_length or row < 0) and (col >= col_length or col < 0):

                    col -= 1
                    row += 2
                
                elif row >= row_length or row < 0:

                    row += 1
                
                elif col >= col_length or col < 0:

                    row += 2
                    col -= 1
            
                up = False
            
            else:

                while row < row_length and row >= 0 and col < col_length and col >= 0:

                    result.append(mat[row][col])

                    row += 1
                    col -= 1

                if (row >= row_length or row < 0) and (col >= col_length or col < 0):

                    col += 2
                    row -= 1
                
                elif  row >= row_length or row < 0:

                    row -= 1
                    col += 2
                
                elif col >= col_length or col < 0:

                    col += 1
            
                up = True
        
        return result

                

