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
                    self.swap(nums,j,j+1)
    def swap(self,nums,x,y):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp
