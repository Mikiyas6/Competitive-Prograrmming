class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        

        result = []
        visited = set()
        direction_index = 0 
        steps = 1
        total_cells = rows * cols
        
        x, y = rStart, cStart
        

        while len(result) < total_cells:
            for _ in range(2):  
                for _ in range(steps):
                  
                    if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited:
                        result.append([x, y])
                        visited.add((x, y))
            
                    x += directions[direction_index][0]
                    y += directions[direction_index][1]
                    

                direction_index = (direction_index + 1) % 4
            
         
            steps += 1
        
        return result