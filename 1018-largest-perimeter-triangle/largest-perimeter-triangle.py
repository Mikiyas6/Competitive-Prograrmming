class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        area = 0
        maxArea = 0

        for right in range(2,len(nums)):
            if nums[right-2] + nums[right-1] > nums[right]:
                area = nums[right-2] + nums[right-1] + nums[right]
                maxArea = max(maxArea,area)
        
        return maxArea