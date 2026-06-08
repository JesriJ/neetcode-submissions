class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # # Brute Force
        # return min(nums)

        # # Optimal
        # l = 0
        # r = len(nums)-1

        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] < nums[r]:
        #         r = m
        #     else:
        #         l += 1
        # return nums[l]

        # Classic Binary Search

        # l = 0
        # r = len(nums) - 1
        # res = nums[0]

        # while l <= r:
        #     m = (l + r) // 2
        #     res = min(res, nums[m])
        #     if nums[m] >= nums[l]:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return res

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
 


