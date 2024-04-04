class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def binary_search(s,e):
    
            if s == e:
                
                return s
            
            mid = (s+(e-s)//2)
            
            if arr[mid] > arr[mid+1]:

                e = mid
            
            else:

                s = mid + 1
                    
            return binary_search(s,e)
        
        return binary_search(0,len(arr)-1)