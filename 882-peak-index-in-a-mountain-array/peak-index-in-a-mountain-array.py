class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def find_peak_element(s,e):
    
            if s == e:
                return s
            
            mid = s + (e-s)//2
            
            if arr[mid] < arr[mid+1]:
                s = mid+1
            else:
                e = mid
            
            return find_peak_element(s,e)

        s, e = 0, len(arr)-1
        return find_peak_element(s,e)