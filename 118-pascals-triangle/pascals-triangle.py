class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        grid = [[0]*numRows for _ in range(numRows)]
        for i in range(numRows):
            grid[i][0] = 1
        for row in range(1,numRows):
            for col in range(1,numRows):
                grid[row][col] = grid[row-1][col-1] + grid[row-1][col]
        
        for i in range(numRows):
            grid[i] = grid[i][:i+1]
        return grid