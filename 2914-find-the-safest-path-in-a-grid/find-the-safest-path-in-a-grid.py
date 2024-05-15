class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
    
        # Step 1: Collect all thief positions
        thief_positions = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 1]

        # Step 2: Calculate minimum distances to any thief for each cell using multi-source BFS
        min_dist_to_thief = [[float('inf')] * n for _ in range(n)]
        queue = deque(thief_positions)
        for r, c in thief_positions:
            min_dist_to_thief[r][c] = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and min_dist_to_thief[nr][nc] == float('inf'):
                    min_dist_to_thief[nr][nc] = min_dist_to_thief[r][c] + 1
                    queue.append((nr, nc))

        # Step 3: Use a max-heap to perform Dijkstra's algorithm to find the maximum safeness path
        max_heap = [(-min_dist_to_thief[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        
        while max_heap:
            safeness, r, c = heappop(max_heap)
            safeness = -safeness  # Since we use a max-heap, we stored negative values

            if r == n - 1 and c == n - 1:
                return safeness
            
            if visited[r][c]:
                continue
            
            visited[r][c] = True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    new_safeness = min(safeness, min_dist_to_thief[nr][nc])
                    heappush(max_heap, (-new_safeness, nr, nc))
        
        return 0