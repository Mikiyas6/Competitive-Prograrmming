class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def inbound(row,col):
            return 0 <= row and row < m and 0 <= col and col < n

        def DFS(row,col,visited):

            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy
                if inbound(newRow,newCol) and (newRow,newCol) not in visited and grid[newRow][newCol] == "1":
                    visited.add((newRow,newCol))
                    DFS(newRow,newCol,visited)

        m = len(grid)
        n = len(grid[0])
        visited = set()
        counter = 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        for row in range(m):
            for col in range(n):
                if (row,col) not in visited and grid[row][col] == '1':
                    visited.add((row,col))
                    counter += 1
                    DFS(row,col,visited)
        return counter
