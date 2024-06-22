class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for index,value in enumerate(nums):

            if value %2 == 0:

                nums[index] = 0
            
            else:
                
                nums[index] = 1
        
        hashmap = defaultdict(int)

        hashmap[0] = 1

        total = 0

        count = 0

        for r in range(len(nums)):

            total += nums[r]

            if total - k in hashmap:

                count += hashmap[total-k]
            
            hashmap[total] += 1

        return count

