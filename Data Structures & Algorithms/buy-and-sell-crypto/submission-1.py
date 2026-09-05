class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 0
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:               # If buy is less than sell price
                profit = prices[r] - prices[l]          # Calculate local profit
                maxProfit = max(maxProfit, profit)      # Is local profit more than all-time?
            else:                                   # If sell is less than buy
                l = r                                   # Better sell price, go to r
            r += 1                                  # shift right pointer to right

        return maxProfit