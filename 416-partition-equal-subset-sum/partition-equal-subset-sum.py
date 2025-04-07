class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = defaultdict(int)
        total = sum(nums)
        targetSum = total//2

        if total %2 != 0:
            return False

        def fun(i, total):
            
            if i >= n or total > targetSum:
                return False
            if total == targetSum:
                return True
            
            if (i, total) not in memo:
                memo[(i,total)] = fun(i+1,total+nums[i]) or fun(i+1,total)
            
            return memo[(i,total)]
        
        return fun(0,0)