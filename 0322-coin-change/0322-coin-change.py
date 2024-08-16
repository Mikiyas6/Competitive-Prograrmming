class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            minCoins = float('inf')
            for coin in coins:
                remainder = i - coin
                if remainder >= 0:
                    minCoins = min(minCoins,dp[remainder])
            dp[i] = minCoins + 1
        return dp[-1] if dp[-1] != float('inf') else -1

        # memo = defaultdict(int)

        # def fun(total):
        #     if total in memo:
        #         return memo[total]

        #     if total == 0:
        #         return 0

        #     if total < 0:
        #         return float('inf')

        #     minCoins = float('inf')
        #     for value in coins:
        #         minCoins = min(minCoins, fun(total - value))

        #     memo[total] = minCoins + 1
        #     return memo[total]

        # result = fun(amount)
        # return result if result != float('inf') else -1

        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0

        # for coin in coins:
        #     for x in range(coin, amount + 1):
        #         dp[x] = min(dp[x], dp[x - coin] + 1)
                
        # return dp[amount] if dp[amount] != float('inf') else -1
            