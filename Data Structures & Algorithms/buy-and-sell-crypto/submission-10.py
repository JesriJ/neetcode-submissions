class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # maxP = 0
        # minBuy = prices[0]

        # for p in prices:
        #     maxP = max(maxP, p - minBuy)
        #     minBuy = min(minBuy, p)
        
        # return maxP

        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            maxP = max(maxP, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return maxP
