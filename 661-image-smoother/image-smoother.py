class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        row_length = len(img)
        col_length = len(img[0])
        
        new_matrix = [[0]*len(img[0]) for _ in range(len(img))]

        def bounds(row,col):

            total = img[row][col]

            counter = 1

            if row-1 >= 0:

                total += img[row-1][col]
                counter += 1
            
            if row + 1 < row_length:

                total += img[row+1][col]
                counter += 1
            
            if col-1 >= 0:

                total += img[row][col-1]
                counter += 1
            
            if col + 1 < col_length:

                total += img[row][col+1]
                counter += 1
            
            if col-1 >= 0 and row-1 >= 0:

                total += img[row-1][col-1]
                counter += 1
            
            if col + 1 < col_length and row - 1 >= 0:

                total += img[row-1][col+1]
                counter += 1
            
            if row + 1 < row_length and col - 1 >= 0:

                total += img[row+1][col-1]
                counter += 1
            
            if row + 1 < row_length and col + 1 <  col_length:

                total += img[row+1][col+1]
                counter += 1
            
            average = total // counter

            new_matrix[row][col] = average
        
        for row in range(len(img)):

                for col in range(len(img[row])):

                    bounds(row,col)
            
        return new_matrix
        
                

                
