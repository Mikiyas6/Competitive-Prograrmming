class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        minimum = float("inf")
        total = 0

        for r in range(len(nums)):

            total += nums[r]

            while total >= target and l <= r:

                minimum = min(minimum,r-l+1)
                total -= nums[l]
                l += 1
        
        return minimum if minimum != float("inf") else 0
        
