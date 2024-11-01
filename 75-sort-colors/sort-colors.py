class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        # length of the array nums
        n = len(nums)
        # Iterate through the array using two pointers and compare adjacent values
        for i in range(n):
            for j in range(1,n-i):
                # If the value at the leser index is greater, swap the number to bubble up the big number
                if nums[j-1] >= nums[j]:
                    nums[j-1],nums[j] = nums[j], nums[j-1]
        
                