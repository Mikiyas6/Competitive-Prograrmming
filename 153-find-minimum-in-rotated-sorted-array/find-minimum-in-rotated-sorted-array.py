class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        s, e = 0, len(nums) - 1
        n = len(nums)

        def fun(s,e):

            if s > e:

                return -1
            
            mid = s + (e-s)//2

            if mid + 1 < n and nums[mid] > nums[mid+1]:

                return mid
            
            if nums[mid] < nums[mid-1]:

                return mid-1
            
            if nums[s] >= nums[mid]:

                e = mid-1
            
            elif nums[s] < nums[mid]:

                s = mid
            
            return fun(s,e)

        pivot = fun(s,e)

        return nums[pivot+1]