class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def peak(s,e,nums):
            
            if s == e:

                return s

            mid = s + (e-s)//2 
            
            if nums[mid] > nums[mid+1]:

                e = mid
            
            else:

                s = mid + 1
            
            return peak(s,e,nums)
        
        return peak(0,len(nums)-1,nums)