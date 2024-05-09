class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first_and_last(s,e,target,ans,isFirst):
            
            if s > e:
                return ans
            
            mid = s + (e-s)//2
            
            if target < nums[mid]:
                e = mid-1
            elif target > nums[mid]:
                s = mid+1
            else:
                ans = mid
                if isFirst:
                    e = mid-1
                else:
                    s = mid+1
            
            return first_and_last(s,e,target,ans,isFirst)

        s, e = 0, len(nums)-1
        ans = -1
        first = first_and_last(s,e,target,ans,True)
        last = first_and_last(s,e,target,ans,False)
        return [first,last]