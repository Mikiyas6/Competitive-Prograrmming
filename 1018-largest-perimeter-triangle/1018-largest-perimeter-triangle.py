class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        maxArea = 0
        for index in range(2,n):
            if nums[index-2] + nums[index-1] > nums[index]:
                area = nums[index-2] + nums[index-1] + nums[index]
                maxArea = max(maxArea,area)
        return maxArea