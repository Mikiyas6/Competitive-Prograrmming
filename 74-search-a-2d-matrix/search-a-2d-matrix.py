class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n, m = len(matrix), len(matrix[0])
        s, e = 0, m-1

        def fun(s,e):

            if e < 0 or s == n:

                return False
            
            if target == matrix[s][e]:

                return True
            
            if target < matrix[s][e]:

                e -= 1
            
            else:

                s += 1
            
            return fun(s,e)
        
        return fun(s,e)