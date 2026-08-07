class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

            res = 0
            numSet = set(nums)

            for i in range(len(nums)):
                if nums[i]-1 not in numSet:
                    streak = 1
                    while nums[i] + streak in numSet:
                        streak += 1
                    res = max(res, streak)
            
            return res
