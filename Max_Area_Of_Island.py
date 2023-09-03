class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        current_area = 0
        
        def explore_island(grid, visited, index):
            area = 0
            if grid[visited][index] != 1:
                return 0
            grid[visited][index] = 2  # Mark as visited
            area += 1
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for i, j in directions:
                new_row, new_col = visited + i, index + j
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    area += explore_island(grid, new_row, new_col)
            return area
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, explore_island(grid, i, j))
        
        return max_area
