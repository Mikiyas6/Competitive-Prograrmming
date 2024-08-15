class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)

        def fun(total):
            if total in memo:
                return memo[total]

            if total == amount:
                return 0

            if total > amount:
                return float('inf')

            minCoins = float('inf')
            for value in coins:
                minCoins = min(minCoins, fun(total + value) + 1)

            memo[total] = minCoins
            return minCoins

        result = fun(0)
        return result if result != float('inf') else -1

        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0

        # for coin in coins:
        #     for x in range(coin, amount + 1):
        #         dp[x] = min(dp[x], dp[x - coin] + 1)
                
        # return dp[amount] if dp[amount] != float('inf') else -1
            