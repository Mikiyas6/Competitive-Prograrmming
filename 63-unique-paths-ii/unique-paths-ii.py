class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0]*(m) for _ in range(n)]

        for i in range(n):
            if not obstacleGrid[i][0]:
                dp[i][0] = 1
            else:
                for row in range(i,n):
                    for col in range(1):
                        dp[row][col] = 0
                break
                
        for j in range(m):
            if not obstacleGrid[0][j]:
                dp[0][j] = 1
            else:
                for row in range(1):
                    for col in range(j,m):
                        dp[row][col] = 0
                break
        
        for row in range(1,n):
            for col in range(1,m):
                if not obstacleGrid[row][col]:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[n-1][m-1]

        # n, m = len(obstacleGrid), len(obstacleGrid[0])
        # memo = defaultdict(int)

        # def inbound(row,col):
        #     return 0 <= row and row < n and 0 <= col and col < m and not obstacleGrid[row][col]
        
        # def fun(row,col):

        #     if not inbound(row,col):
        #         return 0
            
        #     if row == n-1 and col == m-1:
        #         return 1
            
        #     if (row,col) not in memo:
        #         memo[(row,col)] = fun(row+1,col) + fun(row,col+1)
            
        #     return memo[(row,col)]
        
        # return fun(0,0)