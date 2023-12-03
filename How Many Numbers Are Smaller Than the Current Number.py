class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)
        
        hashmap = defaultdict(int)

        for value in sorted_nums:

            hashmap[value] += 1
        
        total = 0

        hashmap1 = defaultdict(int)

        for value,count in hashmap.items():

            hashmap1[value] = total
            total += count
        
        output = []
        
        for value in nums:

            output.append(hashmap1[value])
        
        return output
