class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = defaultdict(int)
        
        def fun(i,total):

            if i >= len(nums):
                if total == target:
                    return 1
                return 0

            if (total,i) not in memo:
                memo[(total,i)] = fun(i+1,total+nums[i]) + fun(i+1,total-nums[i])
            
            return memo[(total,i)]
        
        return fun(0,0)
