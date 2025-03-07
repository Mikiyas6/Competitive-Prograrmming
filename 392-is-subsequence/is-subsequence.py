class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = len(t)-1
        i = len(s)-1
        if not t:
            if s:
                return False
            return True
        while i >= 0:
            flag = False
            while s[i] != t[j]:
                flag = True
                j -= 1
                if j < 0:
                    break
            if j < 0:
                break
            j -= 1
            i -= 1
        return False if i >= 0 else True

        
