class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_day = prices[0]
        for price in prices[1:]:
            if price > buy_day:
                profit = max(profit,price-buy_day)
            buy_day = min(buy_day,price)
        return profit
