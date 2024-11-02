class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        def flip(left,right):

            while left <= right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        
        k %= n

        flip(0,n-k-1)
        flip(n-k,n-1)
        flip(0,n-1)
