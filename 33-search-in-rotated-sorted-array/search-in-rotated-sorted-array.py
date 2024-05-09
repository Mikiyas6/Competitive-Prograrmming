class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(s,e,target):

            if s > e:
                return -1
            
            mid = s + (e-s)//2

            if target == nums[mid]:
                return mid                
            elif target < nums[mid]:
                e = mid-1
            else:
                s = mid+1
            
            return binary_search(s,e,target)
                  
        def find_pivot(s,e):

            if s > e:
                return -1
            
            mid = s + (e-s)//2

            if mid+1 < n and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] < nums[mid-1]:
                return mid-1
            
            if nums[s] >= nums[mid]:
                e = mid-1
            else:
                s = mid+1
            
            return find_pivot(s,e)
         
        n = len(nums)
        s, e = 0, n-1

        pivot = find_pivot(s,e)

        if pivot == -1:
            normal = binary_search(s,e,target)
            return normal
        
        if nums[pivot] == target:
            return pivot
        
        left = binary_search(s,pivot-1,target)
        right = binary_search(pivot+1,e,target)

        return max(left,right)



        