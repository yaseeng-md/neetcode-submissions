from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):

            # find the highest element after buying 
            price_diff = max(prices[i+1:]) - prices[i]
            if price_diff > max_profit:
                max_profit = price_diff
        return max_profit
