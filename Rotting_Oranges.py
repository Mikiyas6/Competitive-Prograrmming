from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        queue = deque()
        minutes = 0
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                
        while queue:
            row, col, curr_minutes = queue.popleft()
            minutes = max(minutes, curr_minutes)  
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col, curr_minutes + 1))

        
        for row in grid:
            if 1 in row:
                return -1

        return minutes
