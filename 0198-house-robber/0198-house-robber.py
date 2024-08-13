class Solution:
    def rob(self, nums: List[int]) -> int:

        # memo = defaultdict(int)

        # def fun(i):
        #     if i >= len(nums):
        #         return 0
            
        #     if i not in memo:
        #     # Option 1: Rob the current house and skip one
        #     # Option 2: Skip the current house
        #         memo[i] = max(nums[i] + fun(i + 2), fun(i + 1))
        #     return memo[i]
        
        # return fun(0)

        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*(n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        
        return dp[n-1]