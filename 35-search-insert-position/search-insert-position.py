class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1

        def ceil(nums,start,end,target):
            if start > end:
                return start
            mid = start + (end-start)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
            return ceil(nums,start,end,target)
        
        return ceil(nums,start,end,target)
            