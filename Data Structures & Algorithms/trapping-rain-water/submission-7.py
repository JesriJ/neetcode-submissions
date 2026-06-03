class Solution:
    def trap(self, height: List[int]) -> int:
        
        # # Bruteforce
        # res = 0
        # for i in range(len(height)):
        #     leftMax = rightMax = height[i]

        #     for j in range(i):
        #         leftMax = max(leftMax, height[j])
            
        #     for j in range(i+1, len(height)):
        #         rightMax = max(rightMax, height[j])
            
        #     res += min(leftMax, rightMax) - height[i]
        
        # return res

        if not height:
            return 0

        l = 0
        r = len(height)-1
        res = 0
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
        return res
