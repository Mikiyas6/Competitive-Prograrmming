class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        n = len(nums)

        cumulative = 0

        prefix_sum = []

        for index,value in enumerate(nums):

            cumulative += value

            prefix_sum.append(cumulative)
        
        return prefix_sum

