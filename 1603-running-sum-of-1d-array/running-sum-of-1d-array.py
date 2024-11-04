class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        result = []

        for value in nums:
            total += value
            result.append(total)
        
        return result