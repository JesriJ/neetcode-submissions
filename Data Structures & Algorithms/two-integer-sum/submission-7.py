class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}
        l = []

        for i in range(len(nums)):
            val = target-nums[i]
            if val in m:
                l.append(m[val])
                l.append(i)
                return l
            m[nums[i]] = i
         