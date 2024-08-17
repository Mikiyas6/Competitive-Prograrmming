class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = defaultdict(int)
        def dp(i, target_sum):
            if i >= n or target_sum <= 0:
                return target_sum == 0
            
            state = (i, target_sum)
            if state not in memo:
                memo[state] = dp(i + 1, target_sum - nums[i]) or dp(i + 1, target_sum)
            
            return memo[state]
        
        return sum(nums) % 2 == 0 and dp(0, sum(nums) // 2)