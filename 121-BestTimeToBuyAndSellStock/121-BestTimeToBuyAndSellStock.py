# Last updated: 2/21/2026, 9:44:32 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy_amount=max(prices)
        for price in prices:
            if price<buy_amount:
                buy_amount=price
            max_profit=max(max_profit,price-buy_amount)
        return max_profit
        