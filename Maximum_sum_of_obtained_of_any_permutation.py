class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        prefix_sum = [0] * (len(nums)+1)

        for start, end in requests:

            prefix_sum[start] += 1
            prefix_sum[end+1] -= 1
        
        cumulative = 0
        
        for index,value in enumerate(prefix_sum):

            cumulative += value
            prefix_sum[index] = cumulative
        
        prefix_sum = prefix_sum[:len(nums)]
        
        nums.sort()
        prefix_sum.sort()

        sum_of_product = 0

        for r in range(len(nums)):

            sum_of_product += nums[r] * prefix_sum[r]
        
        return sum_of_product % (10**9 + 7)


