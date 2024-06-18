class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        visited = set()
        area, maxArea = 1, 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def inbound(row,col):
            return 0 <= row and row < n and 0 <= col and col < m

        def dfs(row,col):

            nonlocal area
            for dx, dy in directions:
                newRow = row+dx
                newCol = col+dy

                if inbound(newRow,newCol) and (newRow,newCol) not in visited and grid[newRow][newCol] == 1:
                    visited.add((newRow,newCol))
                    area += 1
                    dfs(newRow,newCol)
            
            return 
        
        for row in range(n):
            for col in range(m):
                if (row,col) not in visited and grid[row][col]:
                    visited.add((row,col))
                    dfs(row,col)
                    maxArea = max(maxArea,area)
                    area = 1
        
        return maxArea
