class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_array = sorted(nums)

        hashmap = defaultdict(int)

        for index,value in enumerate(sorted_array):

            if value not in hashmap:

                hashmap[value] = index
        
        output = []

        for value in nums:

            output.append(hashmap[value])
        
        return output
