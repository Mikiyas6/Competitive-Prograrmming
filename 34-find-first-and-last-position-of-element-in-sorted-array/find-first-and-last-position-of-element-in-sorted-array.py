class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(s,e,target,side):
    
            ans = -1
            
            while s <= e:
                
                mid = s + (e-s)//2
                
                if target > nums[mid]:
                
                    s = mid + 1
            
                elif target < nums[mid]:
                    
                    e = mid - 1
                
                else: 
                    
                    ans = mid
                    
                    if side == "first":
                        
                        e = mid - 1
                    
                    else:
                        
                        s = mid + 1
                
            return ans

        first = binary_search(0,len(nums)-1,target,"first")

        last = binary_search(0,len(nums)-1,target,"last")

        return [first,last]


        