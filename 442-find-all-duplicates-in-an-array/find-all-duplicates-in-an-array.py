class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        return [value for value in hashmap if hashmap[value] == 2]