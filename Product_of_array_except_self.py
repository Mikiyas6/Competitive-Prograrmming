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





