class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices or len(prices) == 1:

            return 0
        
        l = 0 # The day we buy

        max_profit = 0

        for r in range(1,len(prices)): # r is the day we say our stock

            if prices[r] <= prices[l]:

                l = r
            
            else:

                profit = prices[r] - prices[l]
                max_profit = max(max_profit,profit)

        return max_profit




        

