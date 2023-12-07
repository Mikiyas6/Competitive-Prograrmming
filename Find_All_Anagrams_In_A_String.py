class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        k = len(p)

        n = len(s)
        
        p_hashmap = Counter(p)
        s_hashmap = Counter(s[:k])

        output = []

        if p_hashmap == s_hashmap:

            output.append(0)
        
        l = 0

        for r in range(k,n):

            s_hashmap[s[l]] -= 1
            s_hashmap[s[r]] += 1

            if s_hashmap[s[l]] == 0:

               s_hashmap.pop(s[l])
            
            if s_hashmap == p_hashmap:

                output.append(l+1)

            l += 1
        
        return output
        

