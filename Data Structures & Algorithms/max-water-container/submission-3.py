class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # # Brute Force
        # res = 0
        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         res = max(res, min(heights[l], heights[r]) * (r-l))
        
        # return res

        # Optimal
        l = 0
        r = len(heights)-1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r-l))
            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1
        
        return res