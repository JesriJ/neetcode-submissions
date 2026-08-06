class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Initiate array with 1s and length of nums
        res = [1] * (len(nums))

        #Set prefix values to each element shifting one to the right, index 0 should have prefix of 1
        prefix=1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        #Multiply each prefix in array with postfix
        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
              
        
        #Return Array
        return res
