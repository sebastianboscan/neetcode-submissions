class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxP = 0

        for i in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP       

        # Reasoning: We are always on the lookout for a cheaper buy price, the moment we see an opportunity for profit
        #            we calculate it and check if its more than our current max profit.

        # Solution: Always work with the cheapest price, and always get your max profit given min price - current price.

        # Takeaways: Use your pointers where most appropiate and draw a test case to walk through the algorithm.