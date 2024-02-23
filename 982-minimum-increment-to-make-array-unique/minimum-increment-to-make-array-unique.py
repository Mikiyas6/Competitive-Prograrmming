class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        moves = 0
        prev = nums[0]
        
        for i in range(1, len(nums)):
    
            if nums[i] <= prev:
                moves += prev - nums[i] + 1
                nums[i] = prev + 1
                
            prev = nums[i]
        
        return moves