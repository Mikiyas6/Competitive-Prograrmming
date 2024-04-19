class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(0,1),(-1,0),(1,0),(0,-1)]

        def inbound(row,col):

            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        def dfs(row,col):

            if grid[row][col] == "0" or not inbound(row,col):
                return

            grid[row][col] = "2"
            
            for dx, dy in directions:

                new_row = row + dx
                new_col = col + dy

                if not inbound(new_row,new_col) or grid[new_row][new_col] == "2" or grid[new_row][new_col] == "0":
                    continue
                grid[new_row][new_col] == "2"
                dfs(new_row,new_col)
            return

        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    print(i,j)
                    counter += 1
                    dfs(i,j)

        return counter