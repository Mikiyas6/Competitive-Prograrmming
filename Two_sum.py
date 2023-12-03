class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = defaultdict(int)

        for index,value in enumerate(nums):

            diff = target - value

            if diff in hashmap:

                return [hashmap[diff],index]
            
            hashmap[value] = index
            
