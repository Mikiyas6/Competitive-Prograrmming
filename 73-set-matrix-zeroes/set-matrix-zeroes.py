class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroPositions = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroPositions.append([i,j])
        for row,col in zeroPositions:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            for j in range(len(matrix)):
                matrix[j][col] = 0
        