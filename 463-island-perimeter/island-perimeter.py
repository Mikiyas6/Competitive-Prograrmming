class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def inbound(row,col):
            return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])

        def dfs(row,col):

            if not inbound(row,col) or grid[row][col] == 0:
                return 1
            
            perimeter = 0
            visited.add((row,col))

            for dx, dy in directions:
                newRow = row+dx
                newCol = col+dy
                if (newRow,newCol) not in visited:
                    perimeter += dfs(newRow,newCol)
                    
            return perimeter
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row,col)
            