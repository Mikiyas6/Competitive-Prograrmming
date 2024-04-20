class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        def dfs(r, c):
            nonlocal top_left, bottom_right
            if r < 0 or r >= len(land) or c < 0 or c >= len(land[0]) or land[r][c] != 1:
                return
            land[r][c] = -1  # Mark cell as visited
            top_left = [min(top_left[0], r), min(top_left[1], c)]
            bottom_right = [max(bottom_right[0], r), max(bottom_right[1], c)]
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        result = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    top_left = [i, j]
                    bottom_right = [i, j]
                    dfs(i, j)
                    result.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])

        return result