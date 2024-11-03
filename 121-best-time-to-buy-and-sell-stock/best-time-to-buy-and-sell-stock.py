class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        bestOne = prices[0]
        for price in prices[1:]:
            if price < bestOne:
                bestOne = price
            maxProfit = max(maxProfit,price-bestOne)
        return maxProfit
