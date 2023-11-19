class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cumulative = 0
        max_sum = float("-inf")

        for value in nums:

            if cumulative < 0:

                cumulative = value
            
            else:

                cumulative += value
            
            max_sum = max(max_sum,cumulative)
        
        return max_sum
