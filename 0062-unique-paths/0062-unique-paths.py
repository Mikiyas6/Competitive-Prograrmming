class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1]*(n+1) for _ in range(m+1)]

        for row in range(1,len(dp)):
            for col in range(1,len(dp[0])):
                dp[row][col] = dp[row-1][col] + dp[row][col-1] 

        return dp[m-1][n-1]

        # memo = defaultdict(int)

        # def inbound(row,col):
        #     return 0 <= row and row < m and 0 <= col and col < n
        
        # def dp(row,col):

        #     if row == m-1 and col == n-1:
        #         return 1
            
        #     if not inbound(row,col):
        #         return 0
            
        #     if (row,col) not in memo:
        #         memo[(row,col)] = dp(row+1,col) + dp(row,col+1)
            
        #     return memo[(row,col)]
        
        # return dp(0,0)
            