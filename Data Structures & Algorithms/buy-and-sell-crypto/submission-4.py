class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price: int = prices[0]
        max_profit: int = 0

        for i in range(1,len(prices)):
            profit: int = prices[i] - buy_price
            max_profit = max(profit, max_profit)
            buy_price = min(prices[i], buy_price)
        
        return max_profit
