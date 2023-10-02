from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            first_island.append((i, j))
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        first_island = []
        found_first_island = False
        
        for i in range(n):
            if found_first_island:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found_first_island = True
                    break
        
        queue = deque(first_island)
        sea_cells = set()
        distance = 0
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return distance
                        elif grid[x][y] == 0:
                            grid[x][y] = 2
                            queue.append((x, y))
                            sea_cells.add((x, y))
            distance += 1
        
        while sea_cells:
            for i, j in list(sea_cells):
                sea_cells.remove((i, j))
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return distance - 1
                        elif grid[x][y] == 0:
                            grid[x][y] = 2
                            sea_cells.add((x, y))
            distance += 1
        
        return -1 
