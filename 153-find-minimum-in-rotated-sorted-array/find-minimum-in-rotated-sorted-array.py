class Solution:
    def findMin(self, nums: List[int]) -> int:
                  
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

        if pivot == -1: #Means the array is not rotated so return the first value
            return nums[0]
        
        return nums[pivot+1]
        
        


        