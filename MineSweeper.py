class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        click_row, click_col = click[0], click[1]  
        
        if board[click_row][click_col] == 'M':
            board[click_row][click_col] = 'X'
            return board
        
        num_rows, num_cols = len(board), len(board[0])  
        
        def dfs(row, col):
            if row in [-1, num_rows] or col in [-1, num_cols] or board[row][col] != 'E':
                return
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
            mines = 0
            for dx, dy in directions:
                neighbor_row, neighbor_col = row + dx, col + dy
                if neighbor_row in range(num_rows) and neighbor_col in range(num_cols) and board[neighbor_row][neighbor_col] == 'M':
                    mines += 1
            
            if mines:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for dx, dy in directions:
                    neighbor_row, neighbor_col = row + dx, col + dy
                    dfs(neighbor_row, neighbor_col)
                   
        dfs(click_row, click_col)
    
        return board
