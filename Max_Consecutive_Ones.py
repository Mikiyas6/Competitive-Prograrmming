class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l = 0
        longest = 0

        for r in range(len(nums)):

            if nums[r] == 0:

                l = r + 1
            
            else:

                longest = max(longest,r-l+1)
        
        return longest
