class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.old_matrix = matrix
        row_length, column_length = len(self.old_matrix), len(self.old_matrix[0])
        self.new_matrix = [[0]*(column_length+1) for i in range(row_length+1)]
        for row in range(1,len(self.new_matrix)):
            for column in range(1,len(self.new_matrix[0])):
                self.new_matrix[row][column] = self.new_matrix[row-1][column] + self.new_matrix[row][column-1] - self.new_matrix[row - 1][column - 1] + self.old_matrix[row-1][column-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.new_matrix[row2+1][col2+1] - self.new_matrix[row1][col2+1] - self.new_matrix[row2+1][col1] + self.new_matrix[row1][col1]
    
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
