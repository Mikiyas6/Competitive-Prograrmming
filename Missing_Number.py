class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        extended_nums = set(list(range(0,len(nums)+1)))
        if list(extended_nums.difference(nums)):
            return list(extended_nums.difference(nums))[0]
