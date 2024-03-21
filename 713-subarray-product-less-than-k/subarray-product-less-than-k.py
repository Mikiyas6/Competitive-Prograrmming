class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        
        product = 1

        count = 0

        l = 0

        for r in range(n):

            product *= nums[r]

            while l <= r and product >= k:

                product /= nums[l]

                l += 1
            
            count += r + 1 - l
        
        return count