class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        minutes = 0

        def inbound(row,col):
            return 0 <= row and row < len(grid) and 0 <= col and col < len(grid[0])

        def bfs():

            nonlocal minutes
            queue = deque([])
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 2:
                        queue.append([row,col])

            while queue:

                level = len(queue)
                for _ in range(level):
                    rotten = queue.popleft()
                    for dx, dy in directions:
                        newRow = rotten[0]+dx
                        newCol = rotten[1]+dy
                        if inbound(newRow,newCol) and grid[newRow][newCol] == 1:
                            grid[newRow][newCol] = 2
                            queue.append([newRow,newCol])

                minutes += 1
            
        bfs()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        

        return minutes-1 if minutes > 0 else 0
        
