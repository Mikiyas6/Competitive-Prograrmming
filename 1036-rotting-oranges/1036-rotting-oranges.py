class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def BFS(grid):

            m = len(grid)
            n = len(grid[0])
            queue = deque([])
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 2:
                        queue.append([row,col])
            
            def inbound(row,col):
                return 0 <= row and row < m and 0 <= col and col < n
            
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            minutes = 0
            while queue:
                level = len(queue)
                flag = False
                for _ in range(level):
                    row,col = queue.popleft()
                    for dx, dy in directions:
                        newRow = row + dx
                        newCol = col + dy
                        if inbound(newRow,newCol) and grid[newRow][newCol] == 1:
                            flag = True
                            grid[newRow][newCol] = 2
                            queue.append([newRow,newCol])
                if flag:
                    minutes += 1
            print(grid)
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 1:
                        return -1
            
            return minutes
                    
        return BFS(grid)
