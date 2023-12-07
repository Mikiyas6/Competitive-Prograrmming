class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
      hashmap = defaultdict(int)

      max_count = 0

      l = 0

      counter = 0

      for r in range(len(s)):

        hashmap[s[r]] += 1

        counter += 1

        while hashmap[s[r]] > 1:

          hashmap[s[l]] -= 1

          counter -= 1

          l += 1
          
        max_count = max(max_count,counter)

      return max_count
