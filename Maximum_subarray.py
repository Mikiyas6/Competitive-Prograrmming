class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum_so_far = nums[0]
        curr_max = nums[0]
        
        for value in nums[1:]:

            curr_max = max(curr_max+value,value)
            max_sum_so_far = max(max_sum_so_far,curr_max)
        
        return max_sum_so_far
