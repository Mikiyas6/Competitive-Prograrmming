class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        removed_counter = 0
        remained_counter = 0
        for value in set(nums):
            removed_counter += hashmap[value]//2
            remained_counter += hashmap[value] % 2
        return [removed_counter,remained_counter]
