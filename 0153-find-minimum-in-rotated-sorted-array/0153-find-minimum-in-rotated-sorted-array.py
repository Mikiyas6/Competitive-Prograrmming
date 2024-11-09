class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        def findPeakIndex(start,end,nums):
            if start == end:
                return start
            mid = start + (end-start)//2
            if nums[mid] < nums[start] and nums[mid] < nums[start]:
                end = mid
            else:
                if nums[mid] > nums[mid+1]:
                    end = mid
                else:
                    start = mid+1
            return findPeakIndex(start,end,nums)
        n = len(nums)
        start = 0
        end = n-1
        peakIndex = findPeakIndex(start,end,nums)
        return nums[(peakIndex+1)%n]