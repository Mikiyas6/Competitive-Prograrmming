class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_count, one_count, two_count = 0, 0, 0

        for value in nums:

            if value == 0:

                zero_count += 1
            
            elif value == 1:

                one_count += 1
            
            else:

                two_count += 1
        
        sorted_nums = [0] * zero_count + [1] * one_count + [2] * two_count

        for i in range(len(nums)):

            nums[i] = sorted_nums[i]
        
        
