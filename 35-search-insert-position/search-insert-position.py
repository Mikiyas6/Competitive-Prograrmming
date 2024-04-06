class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def ceil(s,e,target):
    
            if s > e:
                
                return s
            
            mid = (s+(e-s)//2)
            
            if nums[mid] == target:
                
                return mid
            
            if target < nums[mid]:
                
                e = mid-1
            
            else:
                
                s = mid+1
            
            return ceil(s,e,target)
        
        return ceil(0,len(nums)-1,target)

                
            

        