class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l = 0
        product = 1
        total = 0

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k and l <= r:
                product /= nums[l]
                l += 1

            total += r - l + 1

        return total
