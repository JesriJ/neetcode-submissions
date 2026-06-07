class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # # Brute Force
        # return min(nums)

        # Optimal
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l += 1
        return nums[l]

        # # Classic Binary Search

        # l = 0
        # r = len(nums)



