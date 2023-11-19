class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for index,value in enumerate(nums):

            if value %2 == 0:

                nums[index] = 0
            
            else:

                nums[index] = 1
        
        cumulative = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0

        for value in nums:

            cumulative += value

            if cumulative - k in hashmap:

                count += hashmap[cumulative-k]
            
            hashmap[cumulative] += 1
        
        return count
        


        
