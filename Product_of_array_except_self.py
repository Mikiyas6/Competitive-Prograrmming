class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lists1 = []
        lists2 = []
        product = 1
        for i in range(len(nums)):
            lists1.append(product)
            product *= nums[i]
        product = 1
        lists2 = range(len(nums))
        for j in range(-1,-len(nums)-1,-1):
            lists2[j] = product * lists1[j]
            product *= nums[j]
        return lists2
        






        
        
        
        

        
        
