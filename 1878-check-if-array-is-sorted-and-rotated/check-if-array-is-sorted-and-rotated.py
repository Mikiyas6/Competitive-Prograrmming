class Solution:
    def check(self, nums: List[int]) -> bool:

        n = len(nums)

        def rotator(i,j,nums):

            if i >= j:

                return nums
            
            nums[i], nums[j] = nums[j], nums[i]

            return rotator(i+1,j-1,nums)

        def checker(i):

            if i == n:

                return -1
            
            if nums[i] < nums[i-1]:

                return i
            
            return checker(i+1)

        pivot = checker(1)

        if pivot == -1:

            return True
        
        nums = rotator(pivot,n-1,nums)
        nums = rotator(0,pivot-1,nums)
        nums = rotator(0,n-1,nums)

        pivot = checker(1)

        if pivot > -1:

            return False
        
        return True

        
        # s, e = 0, n - 1

        # def find_pivot(s,e):

        #     if s > e:

        #         return -1
            
        #     mid = s + (e-s)//2
            
        #     if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:

        #         return mid 
            
        #     if nums[mid] < nums[mid-1]:

        #         return mid - 1
            
        #     if nums[s] >= nums[mid]:

        #         e = mid - 1
            
        #     else:

        #         s = mid + 1
            
        #     return find_pivot(s,e)
        
        # pivot = find_pivot(s,e)
        
        # return True