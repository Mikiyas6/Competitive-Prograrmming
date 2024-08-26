class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS = len(dungeon)
        COLS = len(dungeon[0])
        
        dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS-1][COLS-1] = max(1, -1 * dungeon[ROWS-1][COLS-1] + 1)
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if i == ROWS-1 and j == COLS-1:
                    continue
                minimum = min(dp[i][j+1], dp[i+1][j]) 
                value = max(1, minimum - dungeon[i][j])
                dp[i][j] = value
                
        return dp[0][0]