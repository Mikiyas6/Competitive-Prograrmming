class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def inbound(row,col):
            return 0 <= row and row < m and 0 <= col and col < n

        def DFS(row,col,visited):
            
            area = grid[row][col]
            for dx,dy in directions:
                newRow = row + dx
                newCol = col + dy
                if (newRow,newCol) not in visited and inbound(newRow,newCol) and grid[newRow][newCol] == 1:
                    visited.add((newRow,newCol))
                    area += DFS(newRow,newCol,visited)
            return area

        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        maxArea = 0
        for row in range(m):
            for col in range(n):
                if (row,col) not in visited and grid[row][col] == 1:
                    visited.add((row,col))
                    maxArea = max(maxArea,DFS(row,col,visited))
        return maxArea