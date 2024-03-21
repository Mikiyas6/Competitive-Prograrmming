class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
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