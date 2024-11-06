class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = 0
        if nums:
            n        =  len(nums)
            smallest = min(nums)
            m        = sum(nums) - smallest*n
        return m