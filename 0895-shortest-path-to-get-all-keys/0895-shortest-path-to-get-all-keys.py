class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        key_bit = {chr(i + ord('a')): i for i in range(6)}
        lock_bit = {chr(i + ord('A')): i for i in range(6)}
        all_keys = 0
        start = None

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    all_keys |= (1 << key_bit[grid[i][j]])

        queue = deque([(start[0], start[1], 0, 0)]) 
        visited = set((start[0], start[1], 0))
        
        while queue:
            row, col, keys, steps = queue.popleft()
            
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                    cell = grid[newRow][newCol]
                    
                    if cell == '#':
                        continue
                    
                    if cell.islower():
                        new_keys = keys | (1 << key_bit[cell])
                    else:
                        new_keys = keys
                    
                    if cell.isupper() and not (keys & (1 << lock_bit[cell])):
                        continue
                    
                    if new_keys == all_keys:
                        return steps + 1
                    
                    if (newRow, newCol, new_keys) not in visited:
                        visited.add((newRow, newCol, new_keys))
                        queue.append((newRow, newCol, new_keys, steps + 1))
        
        return -1
