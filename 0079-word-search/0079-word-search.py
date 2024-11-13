class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        m, n = len(board), len(board[0])

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        def backtrack(row, col, index, visited):
            if index == len(word):  
                return True
            if not inbound(row, col) or (row, col) in visited or board[row][col] != word[index]:
                return False
            
            visited.add((row, col))  
            for dx, dy in directions:
                newRow, newCol = row + dx, col + dy
                if backtrack(newRow, newCol, index + 1, visited):
                    return True
            visited.remove((row, col))  
            return False
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:  
                    if backtrack(row, col, 0, set()):
                        return True
        return False
