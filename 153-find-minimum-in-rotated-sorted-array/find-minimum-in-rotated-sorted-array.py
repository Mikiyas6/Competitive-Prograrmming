class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        s, e = 0, len(nums) - 1

        def find_pivot(s,e):

            if s > e:

                return -1
            
            mid = s + (e-s)//2
            
            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:

                return mid 
            
            if nums[mid] < nums[mid-1]:

                return mid - 1
            
            if nums[s] >= nums[mid]:

                e = mid - 1
            
            else:

                s = mid + 1
            
            return find_pivot(s,e)
        
        return nums[(find_pivot(s,e)+1)%len(nums)]