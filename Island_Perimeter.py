class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        visited = [[False]*len(grid[0]) for _ in range(len(grid))]

        def inbound(row,col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def dfs(row,col):
            if not inbound(row,col) or grid[row][col] == 0:
                return 1
            if visited[row][col]:
                return 0
            visited[row][col] = True
            perimeter =  dfs(row,col+1)
            perimeter += dfs(row,col-1)
            perimeter += dfs(row-1,col)
            perimeter += dfs(row+1,col)
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)
            



                    



