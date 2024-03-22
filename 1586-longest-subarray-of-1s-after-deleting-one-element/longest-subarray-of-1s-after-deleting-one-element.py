class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        hashmap = defaultdict(int)

        counter = 0

        l = 0

        for r in range(len(nums)):

            hashmap[nums[r]] += 1

            while hashmap[0] > 1:

                hashmap[nums[l]] -= 1

                l += 1
            
            counter = max(counter,r-l)
        
        return counter