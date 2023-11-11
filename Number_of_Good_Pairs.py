class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        dictionary = Counter(nums)
        total = 0

        for value in dictionary.values():

            total += (value * (value-1)) // 2

        return total

