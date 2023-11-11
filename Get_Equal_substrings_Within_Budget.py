class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l = 0
        dictionary = defaultdict(int)
        max_length = 0
        length = 0
        cost = 0

        for r in range(len(s)):

            distance = abs(ord(t[r]) - ord(s[r]))
            cost += distance
            dictionary[r] = distance

            while cost > maxCost:

                cost -= dictionary[l]
                l += 1
            
            length = r - l + 1
            
            max_length = max(max_length, length)
        
        return max_length

