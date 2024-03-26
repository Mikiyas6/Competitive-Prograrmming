class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total = nums[0]
        max_sum = total

        for value in nums[1:]:

            if total < 0:

                total = value
            
            else:

                total += value
            
            max_sum = max(max_sum,total)
        
        return max_sum
        

        