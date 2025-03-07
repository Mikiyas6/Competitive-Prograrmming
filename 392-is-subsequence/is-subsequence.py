class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s):
            value = s[i]
            while j < len(t) and value != t[j]:
                j += 1
            if j >= len(t):
                break
            i += 1
            j += 1
        return False if i < len(s) else True
                
        

        
