class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        streak = 0
        numsSet = set(nums)

        for n in numsSet:
            if n-1 not in numsSet:
                count = 1
                while n+1 in numsSet:
                    n += 1
                    count += 1
                streak = max(streak, count)

        return streak 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest