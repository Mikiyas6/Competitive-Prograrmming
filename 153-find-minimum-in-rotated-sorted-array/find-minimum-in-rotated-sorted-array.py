class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findMinIndex(start,end,nums):
            if nums[start] <= nums[end]:
                return start
            mid = start + (end-start)//2
            if nums[mid] >= nums[start]:
                start = mid+1
            else:
                end = mid
            return findMinIndex(start,end,nums)
        start = 0
        end = len(nums)-1
        minIndex = findMinIndex(start,end,nums)
        return nums[minIndex]