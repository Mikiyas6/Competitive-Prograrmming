class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        maximum = 0
        while end >= start:
            value = start if arr[start] > arr[end] else end
            maximum = maximum if arr[maximum] > arr[value] else value
            middle = start + (end-start)//2
            maximum = maximum if arr[maximum] > arr[middle] else middle
            end -= 1
            start += 1
        return maximum
