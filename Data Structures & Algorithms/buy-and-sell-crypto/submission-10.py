class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l = buying, r = selling
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            elif prices[l] > prices[r]:
                l = r
            r += 1
        return maxP
