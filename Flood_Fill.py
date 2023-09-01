class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(image), len(image[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        
        def dfs(row, col, starting_color):
            image[row][col] = color
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if 0 <= new_row < rows and 0 <= new_col < cols and visited[new_row][new_col] == 0 and image[new_row][new_col] == starting_color:
                    visited[new_row][new_col] = 1
                    dfs(new_row, new_col, starting_color)
        
        starting_color = image[sr][sc]
        dfs(sr, sc, starting_color)
        
        return image
