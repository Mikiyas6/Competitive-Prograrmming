class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)

        total = sum(nums[:k])
        
        max_sum = total

        l = 0

        for r in range(k,n):

            total = total - nums[l] + nums[r]

            max_sum = max(max_sum,total)
        
            l += 1
        
        return max_sum/k