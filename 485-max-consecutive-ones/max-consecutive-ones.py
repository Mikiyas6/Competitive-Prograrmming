class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        left = 0

        max_length = 0

        for right in range(len(nums)):

            if nums[right] == 0:

                max_length = max(max_length,right - left)

                left = right + 1
    
        
        return max(max_length,right-left+1)
