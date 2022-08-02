class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = float('inf')
        max_profit = 0
        
        for price in prices:
            min_cost = min(price, min_cost)
            max_profit = max(price - min_cost, max_profit)
        
        return max_profit