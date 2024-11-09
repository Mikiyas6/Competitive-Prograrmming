class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def fun(row,col,matrix,target):
            if row == m or col < 0:
                return False
            
            if matrix[row][col] == target:
                return True
            if target < matrix[row][col]:
                col -= 1
            else:
                row += 1
            return fun(row,col,matrix,target)
        
        return fun(0,n-1,matrix,target)