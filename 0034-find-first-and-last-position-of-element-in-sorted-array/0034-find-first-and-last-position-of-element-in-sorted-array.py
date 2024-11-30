class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findPosition(start,end,nums,target,side,ans):
            if start > end:
                return ans
            mid = start + (end-start)//2
            if target < nums[mid]:
                end = mid-1
            elif target > nums[mid]:
                start = mid+1
            else:
                ans = mid
                if side == 'first':
                    end = mid-1
                else:
                    start = mid+1
            return findPosition(start,end,nums,target,side,ans)

        start = 0
        end = len(nums)-1
        ans = -1
        first = findPosition(start,end,nums,target,'first',ans)
        last = findPosition(start,end,nums,target,'last',ans)
        return [first,last]