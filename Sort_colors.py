class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        max_value = max(nums)

        length = max_value + 1

        frequency = [0] * length

        for i in range(n):

            frequency[nums[i]] += 1
        
        output = [0] * len(nums)
        output_length = 0
        
        for index,item in enumerate(frequency):

            if item != 0:

                width = item
                value = index

                output[output_length:output_length+width] = [value] * width
                output_length += width
        
        for i in range(len(nums)):

            nums[i] = output[i]
        

        # zero_count, one_count, two_count = 0, 0, 0

        # for value in nums:

        #     if value == 0:

        #         zero_count += 1
            
        #     elif value == 1:

        #         one_count += 1
            
        #     else:

        #         two_count += 1
        
        # sorted_nums = [0] * zero_count + [1] * one_count + [2] * two_count

        # for i in range(len(nums)):

        #     nums[i] = sorted_nums[i]
        
        

        for i in range(len(nums)):

            nums[i] = sorted_nums[i]
        
        
