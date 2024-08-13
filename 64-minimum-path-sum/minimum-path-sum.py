class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        memo = defaultdict(int)

        def inbound(row,col):
            return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])
        
        def dp(row,col):

            if not inbound(row,col):
                return float('inf')

            if (row,col) not in memo:
                result = min(dp(row,col-1),dp(row-1,col))
                if result == float('inf'):
                    result = 0
                memo[(row,col)] = result  + grid[row][col]
            
            return memo[(row,col)]
        
        
        result = dp(len(grid)-1,len(grid[0])-1)

        return result
