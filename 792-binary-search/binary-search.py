class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(s,e,target):
    
            while s <= e:
                
                mid = s + (e-s)//2
                
                if target == nums[mid]:
                    return mid
                
                elif target < nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            
            return -1
        
        s, e = 0, len(nums)-1
        return binary_search(s,e,target)