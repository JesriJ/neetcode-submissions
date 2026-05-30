class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_all = 1
        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.append(i)
            else:
                product_all *= nums[i]
        
        output = []

        if len(zeroes) > 1:
            return [0]* len(nums)
        elif len(zeroes) == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(int(product_all))
                else:
                    output.append(0)
        else:
            for i in range(len(nums)):
                output.append(int(product_all/nums[i]))

        return output