class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def convert_num_to_coordinates(num):
            row, col = divmod(num - 1, n)
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col
        
        start = 1
        target = n * n
        visited = set()
        
        moves_queue = deque([(start, 0)])
        visited.add(start)
        
        while moves_queue:
            current_square, current_moves = moves_queue.popleft()
            
            if current_square == target:
                return current_moves
            
            for dice_roll in range(1, 7):
                next_square = current_square + dice_roll
                if next_square > target:
                    break
                
                next_row, next_col = convert_num_to_coordinates(next_square)
                if board[next_row][next_col] != -1:
                    next_square = board[next_row][next_col]
                
                if next_square not in visited:
                    visited.add(next_square)
                    moves_queue.append((next_square, current_moves + 1))
        
        return -1
