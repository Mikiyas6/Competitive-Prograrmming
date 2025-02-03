class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l = 0
        max_length = 1
        for r in range(1,len(nums)):
            if nums[r] > nums[r-1]:
                max_length = max(max_length,r-l+1)
            else:
                l = r
        l = 0
        for r in range(1,len(nums)):
            if nums[r] < nums[r-1]:
                max_length = max(max_length,r-l+1)
            else:
                l = r
        return max_length
