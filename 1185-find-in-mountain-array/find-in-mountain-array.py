# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findPeak(start,end,nums):
            if start == end:
                return start
            mid = start + (end-start)//2
            if nums.get(mid) > nums.get(mid+1):
                end = mid
            else:
                start = mid+1
            return findPeak(start,end,nums)
        def findIndexIncreasing(start,end,nums,target):
            if start > end:
                return float('inf')
            mid = start + (end-start)//2
            if nums.get(mid) == target:
                return mid
            if target < nums.get(mid):
                end = mid-1
            else:
                start = mid+1
            return findIndexIncreasing(start,end,nums,target)
        def findIndexDecreasing(start,end,nums,target):
            if start > end:
                return float('inf')
            mid = start + (end-start)//2
            if nums.get(mid) == target:
                return mid
            if target < nums.get(mid):
                start = mid+1
            else:
                end = mid-1
            return findIndexDecreasing(start,end,nums,target)
        
        start = 0
        end = mountain_arr.length()-1
        peakIndex = findPeak(start,end,mountain_arr)
        if mountain_arr.get(peakIndex) == target:
            return peakIndex
        left_index = findIndexIncreasing(start,peakIndex-1,mountain_arr,target)
        right_index = findIndexDecreasing(peakIndex+1,end,mountain_arr,target)
        result = min(left_index,right_index)
        return result if result != float('inf') else -1
