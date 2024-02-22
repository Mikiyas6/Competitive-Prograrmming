class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        row_length = len(matrix)
        column_length = len(matrix[0])
        
        # new_matrix = [[0]*column_length for _ in range(row_length)]

        new_matrix = []

        for col in range(column_length):

            new_list = []

            for row in range(row_length):

                new_list.append(matrix[row][col])
            
            new_matrix.append(new_list)
        
        return new_matrix

