class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l = 0

        longest = 0

        for r in range(len(s)):

            cost = abs(ord(s[r])-ord(t[r]))

            maxCost -= cost

            while maxCost < 0:

                reduced_cost = abs(ord(s[l])-ord(t[l]))

                maxCost += reduced_cost

                l += 1
            
            longest = max(longest,r-l+1)
        
        return longest