class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        matrix = [[0]*(rowIndex+2) for _ in range(rowIndex+1)]
        matrix[0][1] = 1
        print(matrix)
        def fun(row):
            if row >= len(matrix):
                return
            for col in range(1,len(matrix[0])):
                matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col]
            fun(row+1)
        fun(1)
        return matrix[-1][1:]
