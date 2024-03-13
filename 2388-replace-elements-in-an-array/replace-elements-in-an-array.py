class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        hashmap = defaultdict(int)

        for index, value in enumerate(nums):

            hashmap[value] = index
        
        for old_value, new_value in operations:

            index = hashmap[old_value]

            del hashmap[old_value]

            hashmap[new_value] = index
        
        output = [0] * len(nums)
        
        for index, value in enumerate(hashmap.keys()):

            output[hashmap[value]] = value

        return output

