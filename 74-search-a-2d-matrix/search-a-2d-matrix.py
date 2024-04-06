class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n, m = len(matrix), len(matrix[0])
        
        def binary_search(s,e,target): # search in a 2D matrice sorted in row and column wise
    
            if s == n or e == -1:
                
                return False

            if target == matrix[s][e]:
                
                return True

            if target < matrix[s][e]:
                
                e -= 1
            
            else:
                
                s += 1
            
            return binary_search(s,e,target)
        
        return binary_search(0,m-1,target)