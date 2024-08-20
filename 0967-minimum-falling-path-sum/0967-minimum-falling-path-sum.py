class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        def inbound(row,col):
            return 0 <= row and row < n and 0 <= col and col < m

        n, m = len(matrix), len(matrix[0])
        dp = [[float('inf')]*m for _ in range(n)]

        for i in range(m):
            dp[0][i] = matrix[0][i]
        
        for i in range(1,n):
            for j in range(m):
                leftDiagonal = dp[i-1][j-1] if inbound(i-1,j-1) else float('inf')
                up = dp[i-1][j] if inbound(i-1,j) else float('inf')
                rightDiagonal = dp[i-1][j+1] if inbound(i-1,j+1) else float('inf')
                dp[i][j] = min(rightDiagonal,min(leftDiagonal,up)) + matrix[i][j]
        
        return min(dp[-1])

        # n, m = len(matrix), len(matrix[0])
        # minValue = float('inf')

        # memo = defaultdict(int)

        # def inbound(row,col):
        #     return 0 <= row and 0 <= col and col < m

        # def fun(row,col,total):

        #     if row == n:
        #         return total

        #     if not inbound(row,col):
        #         return float('inf')
            
        #     total += matrix[row][col]

        #     if (row,col,total) not in memo:
            
        #         memo[(row,col,total)] = min(fun(row+1,col-1,total),fun(row+1,col,total),fun(row+1,col+1,total))
        #     return memo[(row,col,total)]

        # for i in range(m):
        #     minValue = min(minValue,fun(0,i,0))
        # return minValue