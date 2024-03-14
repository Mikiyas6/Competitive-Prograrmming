class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hashmap = Counter(nums)

        counter = 0

        for value in hashmap.values():

            counter += (value * (value-1)) // 2

        return counter