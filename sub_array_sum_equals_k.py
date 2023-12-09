class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashmap = defaultdict(int)
        hashmap[0] = 1
        counter = 0
        total = 0

        for r in range(len(nums)):

            total += nums[r]
            gap = total - k

            if gap in hashmap:

                counter += hashmap[gap]
            
            hashmap[total] += 1
        
        return counter
            
