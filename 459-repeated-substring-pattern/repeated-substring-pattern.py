class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        def check_pattern(length):
            if len(s) % length != 0:
                return False
            substr = s[:length]
            for i in range(length, len(s), length):
                if s[i:i+length] != substr:
                    return False
            return True
        
        for i in range(1, len(s)//2 + 1):
            if len(s) % i == 0 and check_pattern(i):
                return True
        
        return False