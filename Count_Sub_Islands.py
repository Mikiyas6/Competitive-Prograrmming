class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        num_rows, num_cols, sub_island_count = len(grid1), len(grid1[0]), 0  # Renamed rows to num_rows, cols to num_cols, and count to sub_island_count
        
        def dfs(x, y):
            if x < 0 or x >= num_rows or y < 0 or y >= num_cols or grid2[x][y] != 1:
                return
            
            grid2[x][y] = 0
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Changed i, z to dx, dy for clarity
            for dx, dy in directions:
                dfs(x + dx, y + dy)
        
        for i in range(num_rows):
            for j in range(num_cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        
        for i in range(num_rows):
            for j in range(num_cols):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    sub_island_count += 1
                    
        return sub_island_count
