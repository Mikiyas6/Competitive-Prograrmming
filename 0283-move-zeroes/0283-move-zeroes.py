class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        n = len(nums)

        # Iterate through nums
        while right < n:
            # If the value on the left pointer is 0, Look for a non zero number by the right pointer
            if nums[left] == 0:
                while right < n and nums[right] == 0:
                    right += 1
                # After finding it, swap the numbers
                if right < n:
                    nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right += 1
        
            
        