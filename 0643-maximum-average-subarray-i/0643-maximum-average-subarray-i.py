class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)
        left = 0
        total = sum(nums[:k])
        maxTotal = total

        for right in range(k,n):
            total -= nums[left]
            total += nums[right]
            maxTotal = max(maxTotal,total)
            left += 1
        
        return maxTotal/k