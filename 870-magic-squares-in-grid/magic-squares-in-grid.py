class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def is_magic_square(grid, r, c):
            # All numbers must be distinct and between 1 to 9
            s = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if num < 1 or num > 9 or num in s:
                        return False
                    s.add(num)
            
            # Check the sums
            sum1 = grid[r][c] + grid[r][c+1] + grid[r][c+2]  # First row
            sum2 = grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]  # Second row
            sum3 = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]  # Third row
            
            sum4 = grid[r][c] + grid[r+1][c] + grid[r+2][c]  # First column
            sum5 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]  # Second column
            sum6 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]  # Third column
            
            sum7 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]  # Diagonal 1
            sum8 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]  # Diagonal 2
            
            return sum1 == sum2 == sum3 == sum4 == sum5 == sum6 == sum7 == sum8 == 15

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic_square(grid, r, c):
                    count += 1
        
        return count