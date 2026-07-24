class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        streak = 0
        numsSet = set(nums)

        for n in numsSet:
            count = 1
            while n-1 in numsSet:
                n -= 1
                count += 1
            streak = max(streak, count)

        return streak 