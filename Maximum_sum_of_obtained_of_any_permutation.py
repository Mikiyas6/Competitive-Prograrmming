class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        frequency = [0] * (len(nums)+1)

        for start,end in requests:

            frequency[start] += 1
            frequency[end+1] -= 1
        
        accumulate = 0
        prefix_sum = [0]*len(nums)

        for i in range(len(nums)):
            accumulate += frequency[i]
            prefix_sum[i] = accumulate
        
        prefix_sum.sort()
        nums.sort()

        total = 0

        for i in range(len(nums)):

            total += prefix_sum[i] * nums[i]
        
        return total%(10**9+7)


        
