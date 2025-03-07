class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s == t or not t:
        #     return True
        # if not t:
        #     if s:
        #         return False
        #     return True
        i = 0
        j = 0
        while i < len(s):
            value = s[i]
            while j < len(t) and value != t[j]:
                print(value)
                j += 1
            if j >= len(t):
                break
            i += 1
            j += 1
        return False if i < len(s) else True
                
        

        
