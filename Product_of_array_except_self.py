class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        right = []
        output = []

        cumulative = 1

        for value in nums:

            left.append(cumulative)
            cumulative *= value
        
        cumulative = 1
        
        for value in nums[::-1]:

            right.append(cumulative)
            cumulative *= value
        
        right = right[::-1]

        for i in range(len(nums)):

            output.append(left[i]*right[i])
        
        return output


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         output = [0]*len(nums)
#         prefix = 1
#         postfix = 1

#         for i in range(len(nums)):

#             output[i] = prefix
#             prefix *= nums[i]
        
#         for j in range(len(nums)-1,-1,-1):

#             output[j] *= postfix
#             postfix *= nums[j]
        
#         return output







