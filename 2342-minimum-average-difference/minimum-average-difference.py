class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
    
        if n == 1:
            return 0
        
        # Compute prefix and suffix sums
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        suffix_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]
        
        min_avg_diff = float('inf')
        min_index = -1
        
        for i in range(n):
            left_avg = prefix_sum[i] // (i + 1)
            if i < n - 1:
                right_avg = suffix_sum[i + 1] // (n - i - 1)
            else:
                right_avg = 0
            
            avg_diff = abs(left_avg - right_avg)
            
            if avg_diff < min_avg_diff:
                min_avg_diff = avg_diff
                min_index = i
        
        return min_index