class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for index,value in enumerate(nums):
            result = target-value
            if result in hashmap:
                return [hashmap[result],index]
            hashmap[value] = index
        