class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        n, m = len(grid), len(grid[0])
    
        # Define the directions and the connections based on the street type
        # From any street, If we wanna go left, we can only do that using [1,4,6] these streets only. 
        directions = {
            1: [(0, -1, [1, 4, 6]), (0, 1, [1, 3, 5])],   # left, right
            2: [(-1, 0, [2, 3, 4]), (1, 0, [2, 5, 6])],   # up, down
            3: [(0, -1, [1, 4, 6]), (1, 0, [2, 5, 6])],   # left, down
            4: [(0, 1, [1, 3, 5]), (1, 0, [2, 5, 6])],    # right, down
            5: [(0, -1, [1, 4, 6]), (-1, 0, [2, 3, 4])],  # left, up
            6: [(0, 1, [1, 3, 5]), (-1, 0, [2, 3, 4])]    # right, up
        }
        
        def inbound(row,col):
            return 0 <= row and row < n and 0 <= col and col < m

        visited = set((0,0))

        def dfs(row, col):
            if (row, col) == (n-1, m-1):
                return True
            
            for dx, dy, valid_next_streets in directions[grid[row][col]]:
                newRow = row+dx
                newCol = col+dy

                if inbound(newRow,newCol) and (newRow, newCol) not in visited and grid[newRow][newCol] in valid_next_streets:
                    visited.add((newRow, newCol))
                    if dfs(newRow, newCol):
                        return True
            return False
        
        return dfs(0, 0)