class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        k = k % n 

        # First

        left, right = 0, n - k - 1 

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]
        
            left += 1
            right -= 1
        
        # Second

        left = n - k

        right = n - 1

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]
        
            left += 1
            right -= 1

        # Third

        left, right = 0, n-1

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]
        
            left += 1
            right -= 1



        
        