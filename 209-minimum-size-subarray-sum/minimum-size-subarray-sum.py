class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0

        min_length = float("inf")

        total = 0

        for r in range(len(nums)):

            total += nums[r]

            while total >= target:

                total -= nums[l]

                min_length = min(min_length,r-l+1)

                l += 1

        return min_length if min_length != float("inf") else 0