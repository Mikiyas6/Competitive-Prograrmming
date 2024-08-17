class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        coins.sort()

        for i in range(n):
            for w in range(1,amount+1):
                if w >= coins[i]:
                    dp[i][w] = dp[i-1][w] + dp[i][w-coins[i]]
                else:
                    dp[i][w] = dp[i-1][w]
        
        return dp[n-1][amount]