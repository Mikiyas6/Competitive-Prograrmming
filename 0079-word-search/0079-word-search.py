class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rowLength, colLength = len(board), len(board[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        path = [[False]*colLength for _ in range(rowLength)]

        def inbound(row,col):
            return 0 <= row and row < rowLength and 0 <= col and col < colLength
        
        def isVisited(row,col):
            return path[row][col]

        def dfs(i,row,col):

            if i == len(word):
                return True

            if not inbound(row,col) or board[row][col] != word[i] or isVisited(row,col):
                return False
            
            path[row][col] = True

            for dx,dy in directions:
                newRow = row + dx
                newCol = col + dy

                if dfs(i+1,newRow,newCol):
                    return True
            
            path[row][col] = False
            
            return False
        
        for row in range(rowLength):
            for col in range(colLength):
                if board[row][col] == word[0]:
                    if dfs(0,row,col):
                        return True
        
        return False
            
