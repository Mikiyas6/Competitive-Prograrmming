class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows, num_cols = len(board), len(board[0])  # Get the number of rows and columns in the board.

        def depth_first_search(row, col):
            if row not in range(num_rows) or col not in range(num_cols) or board[row][col] != 'O':
                return

            board[row][col] = 'W'  # Mark the cell as visited.

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                depth_first_search(new_row, new_col)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Define the four possible directions to move.

        # Traverse the border of the board and start a DFS from 'O' cells.
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or i == num_rows - 1 or j == 0 or j == num_cols - 1:
                    if board[i][j] == 'O':
                        depth_first_search(i, j)

        # Update 'O' cells that were not marked during the DFS to 'X', and restore 'W' cells to 'O'.
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'W':
                    board[i][j] = 'O'
