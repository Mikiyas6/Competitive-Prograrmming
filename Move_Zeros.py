class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        while(i < length):
            if nums[i] == 0:
               nums.append(nums.pop(i))
               i -= 1
               length -= 1
            i += 1
        
