class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def search(start,end,nums,target):
            if start > end:
                return start
            mid = start + (end-start)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
            return search(start,end,nums,target)
        
        start = 0
        end = len(nums)-1
        return search(start,end,nums,target)