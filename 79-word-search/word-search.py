class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        def is_safe(row, col):
            return 0 <= row < m and 0 <= col < n and not journey[row][col]

        def fun(row, col, word):

            if not word:
                return True

            if is_safe(row, col) and board[row][col] == word[0]:

                journey[row][col] = True

                up = fun(row-1, col, word[1:])

                down = fun(row+1, col, word[1:])

                left = fun(row, col-1, word[1:])

                right = fun(row, col+1, word[1:])

                journey[row][col] = False

                if (up or down or left or right):
                    return True

            return False

        journey = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if fun(i, j, word):
                    return True

        return False
