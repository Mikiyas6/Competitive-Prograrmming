class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_xored = 0
        for i in range(1,len(nums)+1):
            all_xored ^= i
        for value in nums:
            all_xored ^= value
        return all_xored 