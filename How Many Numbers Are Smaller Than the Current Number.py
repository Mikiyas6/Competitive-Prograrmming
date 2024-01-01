class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)

        hashmap = defaultdict(int)

        for index, value in enumerate(sorted_nums):

            if value not in hashmap:

                hashmap[value] = index
        
        output = []
        
        for value in nums:

            output.append(hashmap[value])
        
        return output
