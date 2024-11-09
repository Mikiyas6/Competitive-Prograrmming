class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def fun(start,end,nums,target):
            if start > end:
                return -1
            mid = start + (end-start)//2
            if target == nums[mid]:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[mid] < target and target <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            return fun(start,end,nums,target)
        start = 0
        end = len(nums)-1
        return fun(start,end,nums,target)
