class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()

        def inbound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])

        def dfs(row, col):
            if not inbound(row, col) or grid2[row][col] == 0 or (row, col) in visited:
                return True

            visited.add((row, col))
            is_sub_island = True
            if grid1[row][col] == 0:
                is_sub_island = False

            for dx, dy in directions:
                newRow, newCol = row + dx, col + dy
                if not dfs(newRow, newCol):
                    is_sub_island = False

            return is_sub_island

        counter = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and (row, col) not in visited:
                    if dfs(row, col):
                        counter += 1

        return counter