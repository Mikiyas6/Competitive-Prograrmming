class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0

        longest = 0

        hashmap = defaultdict(int)

        for r in range(len(s)):

            hashmap[s[r]] += 1

            while hashmap[s[r]] > 1:

                hashmap[s[l]] -= 1

                l += 1
            
            longest = max(longest,r-l+1)
        
        return longest