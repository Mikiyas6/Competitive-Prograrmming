class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        left, right = 0, 1

        while right < n:

            if nums[left] == nums[right]:

                nums[left] *= 2

                nums[right] = 0
            
            left += 1

            right += 1
        
        left, right = 0, 1

        while right < n:

            if nums[left] != 0:

                left += 1
            
            else:

                if nums[right] != 0:

                    nums[left], nums[right] = nums[right], nums[left]

                    left += 1
            
            right += 1
        
        return nums