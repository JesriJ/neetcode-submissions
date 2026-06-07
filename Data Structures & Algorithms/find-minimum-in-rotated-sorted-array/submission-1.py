class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Brute Force
        return min(nums)

        # Optimal
        l = 0
        r = len(nums)-1
        m = len(nums) // 2

        while l < r:
            if nums[m] < nums[r]:
                r = m
            else:
                l += 1
        return nums[l]

