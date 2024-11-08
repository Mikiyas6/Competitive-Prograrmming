class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def findPeak(start,end,arr):
            if start == end:
                return start
            mid = start + (end-start)//2
            if arr[mid] > arr[mid+1]:
                end = mid
            else:
                start = mid+1
            return findPeak(start,end,arr)
        start = 0
        end = len(arr)-1
        return findPeak(start,end,arr)