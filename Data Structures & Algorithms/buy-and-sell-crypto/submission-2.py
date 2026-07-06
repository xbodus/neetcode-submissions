class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price: int = prices[0]
        max_profit: int = 0

        for i in range(1,len(prices)):
            profit: int = prices[i] - buy_price
            if profit > max_profit:
                max_profit = profit
            if prices[i] < buy_price:
                buy_price = prices[i]
        
        if max_profit > 0:
            return max_profit
        return 0
