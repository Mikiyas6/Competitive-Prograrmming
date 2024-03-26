class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        n = len(nums)
        
        MOD = 10**9 + 7

        prefix_sum = [0] * (n+1)

        for left,right in requests:

            prefix_sum[left] += 1
            prefix_sum[right+1] -= 1
        
        cumulative = 0

        for index, value in enumerate(prefix_sum):

            cumulative += value

            prefix_sum[index] = cumulative
        
        prefix_sum = prefix_sum[:n]

        prefix_sum.sort()

        nums.sort()

        prefix_sum = prefix_sum[::-1]

        nums = nums[::-1]

        cumulative = 0

        for index in range(len(prefix_sum)):

            cumulative += prefix_sum[index] * nums[index]
        
        return cumulative % MOD

        