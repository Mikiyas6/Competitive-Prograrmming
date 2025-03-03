class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])
        max_sum = 0
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if inbound(i-1,j) and inbound(i-1,j-1) and inbound(i-1,j+1)and inbound(i+1,j) and inbound(i+1,j-1) and inbound(i+1,j+1):
                    current = grid[i][j]
                    top = grid[i-1][j] 
                    top_left = grid[i-1][j-1] 
                    top_right = grid[i-1][j+1] 
                    bottom = grid[i+1][j] 
                    bottom_left = grid[i+1][j-1] 
                    bottom_right = grid[i+1][j+1] 
                    total =  current + top + top_left + top_right + bottom + bottom_left + bottom_right
                    max_sum = max(max_sum,total)
        return max_sum