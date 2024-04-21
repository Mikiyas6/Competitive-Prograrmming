class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        nums.sort()

        s, e = 0, n-1

        while s <= e:

            mid = s + (e-s)//2

            if mid == nums[mid]:

                s = mid + 1

            elif mid < nums[mid]:

                e = mid - 1
            
        return s