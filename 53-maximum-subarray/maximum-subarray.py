class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        total = 0
        for value in nums:
            if total < 0:
                total = value
            else:
                total += value
            maxSum = max(maxSum,total)
        return maxSum