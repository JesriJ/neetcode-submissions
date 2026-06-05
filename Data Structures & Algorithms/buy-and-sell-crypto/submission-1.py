class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Brute Force
         
        max_prof = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr_max = prices[j]-prices[i]
                max_prof = max(max_prof, curr_max)
        
        return max_prof


