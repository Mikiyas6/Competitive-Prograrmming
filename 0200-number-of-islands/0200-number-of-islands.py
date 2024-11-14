class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def inbound(row,col):
            return 0 <= row and row < m and 0 <= col and col < n
        
        def backtrack(row,col,visited):

            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy
                if inbound(newRow,newCol) and (newRow,newCol) not in visited and grid[newRow][newCol] == '1':
                    visited.add((newRow,newCol))
                    backtrack(newRow,newCol,visited)
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        visited = set()
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and (row,col) not in visited:
                    visited.add((row,col))
                    backtrack(row,col,visited)
                    count += 1
        return count