class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def find_peak_element(s,e):
    
            if s == e:
                return s
            
            mid = s + (e-s)//2
            
            if nums[mid] < nums[mid+1]:
                s = mid+1
            else:
                e = mid
            
            return find_peak_element(s,e)

        s, e = 0, len(nums)-1
        return find_peak_element(s,e)