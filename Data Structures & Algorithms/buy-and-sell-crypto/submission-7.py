class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Brute Force
        # max_prof = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         curr_max = prices[j]-prices[i]
        #         max_prof = max(max_prof, curr_max)
        
        # return max_prof

        # Optimal

        max_prof = 0
        min_price = prices[0]

        for i in range(len(prices)):
            curr_prof = prices[i] - min_price
            max_prof = max(max_prof, curr_prof)
            min_price = min(min_price, prices[i])

        return max_prof


