class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0

        n = len(nums)

        while right < n:

            if nums[left] == 0 and nums[right] != 0:

                nums[left], nums[right] = nums[right], nums[left]

                left += 1
            
            elif nums[left] != 0:

                left += 1
            
            right += 1
        