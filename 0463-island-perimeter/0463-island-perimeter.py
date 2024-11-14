class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def inbound(row,col):
            return 0 <= row and row < m and 0 <= col and col < n

        def backtrack(row,col,visited):
            if not inbound(row,col) or grid[row][col] == 0:
                return 1
                
            perimeter = 0
            for dx,dy in directions:
                newRow = row + dx
                newCol = col + dy
                if (newRow,newCol) not in visited:
                    if (inbound(newRow,newCol) and grid[newRow][newCol] != 0):
                        visited.add((newRow,newCol))
                    perimeter += backtrack(newRow,newCol,visited)

            return perimeter
             
        m = len(grid)
        n = len(grid[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    visited = set()
                    visited.add((row,col))
                    return backtrack(row,col,visited)