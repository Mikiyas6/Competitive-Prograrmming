class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        queue = deque([(0, 0, 1)])
        visited = set()
        
        while queue:
            x, y, path_len = queue.popleft()
            
            if (x, y) == (n-1, n-1):
                return path_len
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, path_len + 1))
                    visited.add((new_x, new_y))
        
        return -1
