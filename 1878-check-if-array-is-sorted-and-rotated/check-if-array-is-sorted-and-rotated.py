class Solution:
    def check(self, nums: List[int]) -> bool:

        k = 0

        for i in range(1,len(nums)):

            if nums[i] < nums[i-1]:

                k = i
                break
        
        k = k % len(nums)

        i = k
        j = len(nums) -1

        while i < j:

            nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j -= 1
        
        i = 0
        j = k - 1

        while i < j:

            nums[i],nums[j] = nums[j], nums[i]

            i += 1
            j -= 1
        
        i = 0
        j = len(nums)-1

        while i < j:

            nums[i],nums[j] = nums[j], nums[i]

            i += 1
            j -= 1
        
        for i in range(1,len(nums)):

            if nums[i] < nums[i-1]:

                return False
        
        return True

        
        # s, e = 0, len(nums) - 1

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