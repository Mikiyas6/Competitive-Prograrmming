class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:

            return 0
        
        max_sum = float("-inf")
        cumulative = 0

        for value in nums:

            if cumulative <= 0:

                cumulative = value
            
            else:

                cumulative += value
        
            max_sum = max(max_sum,cumulative)
        
        return max_sum
