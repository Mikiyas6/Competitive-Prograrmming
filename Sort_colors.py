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
        
        
