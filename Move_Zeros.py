class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        s = 0
        p = 0

        while s < len(nums):

            if nums[s] != 0:
                nums[s],nums[p] = nums[p], nums[s]
                p += 1
            
            s += 1
        


        
