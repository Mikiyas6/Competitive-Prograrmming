class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            if len(nums) == 1:
                break
            elif nums[i] == 0:
                i += 1
            elif nums[i] != 0 and nums[j] != 0:
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] == 0:
                temp  = nums[i]
                nums[j] = temp
                nums[i] =  0
                j += 1
                i += 1
        
        
        
