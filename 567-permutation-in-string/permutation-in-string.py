class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_length = len(s1)
        s2_length = len(s2)
        
        s1_hashmap = Counter(s1)
        s2_hashmap = Counter(s2[:s1_length])

        if s1_hashmap == s2_hashmap:

            return True
        
        l = 0

        for r in range(s1_length,s2_length):

            s2_hashmap[s2[l]] -= 1
            s2_hashmap[s2[r]] += 1

            if s2_hashmap[s2[l]] == 0:

                del s2_hashmap[s2[l]]
            
            if s1_hashmap == s2_hashmap:

                return True
            
            l += 1
        
        return False