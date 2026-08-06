class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}

        for i, n in enumerate(nums):
            val = target-n
            if val in m:
                return [m[val], i]
            m[n] = i
         