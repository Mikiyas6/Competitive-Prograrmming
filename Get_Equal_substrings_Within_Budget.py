class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        hashmap = defaultdict(int)
        l = 0
        max_length = 0
        remaining_cost = maxCost

        for r in range(len(s)):

            cost = abs(ord(t[r]) - ord(s[r]))
            hashmap[r] = cost
            remaining_cost -=  cost

            while remaining_cost < 0:
                
                remaining_cost += hashmap[l]
                l += 1
            
            max_length = max(max_length,r-l+1)

        return max_length


