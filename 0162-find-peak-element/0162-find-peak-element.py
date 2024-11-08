class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def findPeak(start,end,nums):
            if start == end:
                return start
            mid = start + (end-start)//2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid+1
            return findPeak(start,end,nums)
        
        start = 0
        end = len(nums)-1
        return findPeak(start,end,nums)
            