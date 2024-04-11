class Solution:
    def search(self, nums: List[int], target: int) -> int:

        s, e = 0, len(nums)-1
        
        def pivot(s,e):

            if s > e:

                return -1
            
            mid = s+(e-s)//2

            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:

                return mid
            
            if nums[mid] < nums[mid-1]:

                return mid - 1
            
            if nums[s] >= nums[mid]:

                e = mid - 1
            
            else:

                s = mid
            
            return pivot(s,e)
        
        def binary_search(s,e):

            if s > e:

                return -1
            
            mid = s + (e-s)//2

            if nums[mid] == target:

                return mid
            
            if target > nums[mid]:

                s = mid + 1
            
            else:

                e = mid - 1
            
            return binary_search(s,e)
        
        pivot = pivot(s,e)

        if pivot < 0:

            pivot += len(nums)
        
        if nums[pivot] == target:

            return pivot
        
        return max(binary_search(s,pivot),binary_search(pivot+1,e))