class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n_set = set(nums)
        longest = 0

        for n in n_set:
            if n-1 not in n_set:
                count = 1
                while count+n in n_set:
                    count += 1
                longest = max(count, longest)
        return longest