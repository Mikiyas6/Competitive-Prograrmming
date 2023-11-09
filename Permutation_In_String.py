class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_hashmap = Counter(s1)
        s2_hashmap = Counter(s2[:len(s1)])

        if s1_hashmap == s2_hashmap:
            return True

        l = 0

        for r in range(len(s1),len(s2)):

            s2_hashmap[s2[l]] -= 1
            s2_hashmap[s2[r]] += 1

            if s1_hashmap == s2_hashmap:
                return True
            
            l += 1
        
        return False
            
