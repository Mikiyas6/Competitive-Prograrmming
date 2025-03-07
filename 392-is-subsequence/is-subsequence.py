class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t:
            if s:
                return False
            return True
        j = len(t)-1
        i = len(s)-1
        while i >= 0 and j >= 0:
            while s[i] != t[j]:
                j -= 1
                if j < 0:
                    return False
            j -= 1
            i -= 1
        return False if i >= 0 else True

        
