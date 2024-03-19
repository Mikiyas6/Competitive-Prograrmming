class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        s_length = len(s)
        p_length = len(p)
        
        s_anagram = Counter(s[:p_length])
        p_anagram = Counter(p)

        result = []

        if s_anagram == p_anagram:

            result.append(0)
        
        l = 0

        for r in range(p_length,s_length):

            s_anagram[s[l]] -= 1
            s_anagram[s[r]] += 1

            if s_anagram[s[l]] == 0:

                del s_anagram[s[l]]
            
            if p_anagram == s_anagram:

                result.append(l+1)
            
            l += 1
        
        return result


