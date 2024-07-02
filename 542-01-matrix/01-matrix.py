from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        
    
        result = [[-1] * cols for _ in range(rows)]


        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    result[i][j] = 0

        while queue:
            current_row, current_col = queue.popleft()
            
            for dr, dc in directions:
                neighbor_row, neighbor_col = current_row + dr, current_col + dc
                
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and result[neighbor_row][neighbor_col] == -1:
                    result[neighbor_row][neighbor_col] = result[current_row][current_col] + 1
                    queue.append((neighbor_row, neighbor_col))

        return result
