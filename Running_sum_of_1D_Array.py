class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        lists = [0] * len(nums)
        accumulator = 0

        for i in range(len(nums)):

            accumulator += nums[i]
            lists[i] = accumulator
        
        return lists
