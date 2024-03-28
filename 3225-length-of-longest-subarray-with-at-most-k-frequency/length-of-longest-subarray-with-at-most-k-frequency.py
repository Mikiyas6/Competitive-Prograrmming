class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        n = len(nums)
        
        hashmap = defaultdict(int)

        l = 0

        longest = 0

        for r in range(n):

            hashmap[nums[r]] += 1

            while hashmap[nums[r]] > k:

                hashmap[nums[l]] -= 1

                l += 1
            
            longest = max(longest,r-l+1)
        
        return longest

