class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        opposite_color = 'W' if color == 'B' else 'B'
        
        def is_valid(r, c):
            return 0 <= r < 8 and 0 <= c < 8
        
        def check_direction(dr, dc):
            r, c = rMove + dr, cMove + dc
            count = 0
            
            while is_valid(r, c) and board[r][c] == opposite_color:
                r += dr
                c += dc
                count += 1
            
            if count >= 1 and is_valid(r, c) and board[r][c] == color:
                return True
            return False
        
        for dr, dc in directions:
            if check_direction(dr, dc):
                return True
        
        return False