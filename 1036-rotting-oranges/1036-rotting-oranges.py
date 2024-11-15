class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        def BFS(grid):
            m = len(grid)
            n = len(grid[0])
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            queue = deque([])
            visited = set()
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 2:
                        visited.add((row,col))
                        queue.append([row,col])
            def inbound(row,col):
                return 0 <= row and row < m and 0 <= col and col < n
            minutes = 0
            while queue:
                level = len(queue)
                flag = False
                for _ in range(level):
                    row,col = queue.popleft()
                    for dx,dy in directions:
                        newRow = row + dx
                        newCol = col + dy
                        if inbound(newRow,newCol) and (newRow,newCol) not in visited and grid[newRow][newCol] != 0:
                            visited.add((newRow,newCol))
                            queue.append([newRow,newCol])
                            grid[newRow][newCol] = 2
                            flag = True
                if flag:
                    minutes += 1
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 1:
                        return -1
            return minutes
        
        return BFS(grid)