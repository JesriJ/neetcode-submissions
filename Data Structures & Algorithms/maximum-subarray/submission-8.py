class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSub = nums[0]
        # currSum = 0

        # for n in nums:
        #     if currSum < 0:
        #         currSum = 0
        #     currSum += n
        #     maxSub = max(maxSub, currSum)

        # return maxSub

        # Divide and Conquer

        def dfs(l, r):
            if l > r:
                return float("-inf")
            
            m = (l+r) >> 1

            leftSum = rightSum = curSum = 0

            for i in range(m-1, l-1, -1):
                curSum += nums[i]
                leftSum = max(leftSum, curSum)
            
            curSum = 0
            for i in range(m+1, r+1):
                curSum += nums[i]
                rightSum = max(rightSum, curSum)
            
            return (max(dfs(l, m-1),
                        dfs(m+1, r),
                        leftSum + nums[m] + rightSum))
        return dfs(0, len(nums)-1)

