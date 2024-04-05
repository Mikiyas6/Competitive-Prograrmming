class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(s,e):
    
            if s > e:
                
                return -1
            
            mid = (s+(e-s)//2)
            
            if nums[mid] == target:
                
                return mid
            
            Asc = nums[e] >= nums[s]
            
            if Asc:
                
                if target < nums[mid]:
                
                    e = mid-1
            
                else:
                    
                    s = mid+1
            
            else:
                
                if target < nums[mid]:
                    
                    s = mid+1
                    
                else:
                    
                    e = mid-1
                    
            return binary_search(s,e)
        
        def find_pivot(s,e):
    
            if s == e:
                
                return s
            
            mid = (s+(e-s)//2)
            
            if (nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]) or (nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]):
                
                return mid
            
            if nums[mid] < nums[mid+1] and nums[mid] > nums[mid-1]:

                s = mid + 1
            
            else:

                e = mid - 1
                    
            return find_pivot(s,e)
        
        pivot = nums.index(max(nums))

        if nums[pivot] == target:

            return pivot
        
        left = binary_search(0,pivot-1)

        right = binary_search(pivot+1,len(nums)-1)

        return max(left,right)