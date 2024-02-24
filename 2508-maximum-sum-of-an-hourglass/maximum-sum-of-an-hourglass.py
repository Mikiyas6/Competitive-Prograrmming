class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        row_length = len(grid)
        col_length = len(grid[0])

        max_sum = 0

        for row in range(1,row_length-1):

            for col in range(1,col_length-1):

                sum = grid[row][col]

                left_diagonals = grid[row+1][col-1] + grid[row-1][col-1]

                right_diagonals = grid[row+1][col+1] + grid[row-1][col+1]

                verticals = grid[row+1][col] + grid[row-1][col]

                sum += left_diagonals + right_diagonals + verticals

                max_sum = max(max_sum,sum)
        
        return max_sum


