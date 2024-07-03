class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        visited = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = True
        
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        
        max_dist = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    grid[nx][ny] = grid[x][y] + 1 
                    max_dist = max(max_dist, grid[nx][ny] - 1)
        
        return max_dist