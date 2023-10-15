class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        if len(s) == 1:
            return 1
        
        i = 0
        j = i + 1
        longest = 1

        while j < len(s):

            if s[j] in s[i:j]:
                
                i += 1
            
            else:

                j += 1

                longest = max(longest,len(s[i:j]))
        
        return longest
