class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == len(nums) - i - 1:
                    break
                elif nums[j+1] < nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        # for i in range(1,n):

        #     key = nums[i]
        #     j = i - 1

        #     while j >= 0 and key < nums[j]:

        #         nums[j+1] = nums[j]
        #         j -= 1
            
        #     nums[j+1] = key
        

        
        
        
