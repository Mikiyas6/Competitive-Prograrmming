class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def inbound(row,col):
            return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])

        def dfs(row,col): 

            for dx, dy in directions:
                newRow = row+dx
                newCol = col+dy

                if (newRow,newCol) not in visited and inbound(newRow,newCol) and grid[newRow][newCol] == '1':
                    visited.add((newRow,newCol))
                    dfs(newRow,newCol)
            
            return
        
        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == '1':
                    counter += 1
                    dfs(row,col)
        
        return counter
            

