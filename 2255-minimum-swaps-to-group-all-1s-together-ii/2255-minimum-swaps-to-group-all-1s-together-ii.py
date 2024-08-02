class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        totalOnes = sum(nums)

        if totalOnes == 0 or totalOnes == len(nums):
            return 0
        
        nums = nums + nums
        
        maxOnesInWindow = 0
        currentOnesInWindow = 0
        
        for i in range(totalOnes):
            currentOnesInWindow += nums[i]
        maxOnesInWindow = currentOnesInWindow
        
        for i in range(totalOnes, len(nums)):
            currentOnesInWindow += nums[i] - nums[i - totalOnes]
            maxOnesInWindow = max(maxOnesInWindow, currentOnesInWindow)
        
        return totalOnes - maxOnesInWindow