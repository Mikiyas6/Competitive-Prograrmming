class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0]*len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):

            output[i] = prefix
            prefix *= nums[i]
        
        for j in range(len(nums)-1,-1,-1):

            output[j] *= postfix
            postfix *= nums[j]
        
        return output

