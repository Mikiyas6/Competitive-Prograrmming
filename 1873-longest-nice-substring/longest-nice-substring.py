class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def longestNiceSubstringRecursive(s):
            if len(s) < 2:
                return ""
            for i in range(len(s)):
                if s[i].swapcase() not in s:
                    left = longestNiceSubstringRecursive(s[:i])
                    right = longestNiceSubstringRecursive(s[i+1:])
                    if len(left) >= len(right):
                        return left
                    else:
                        return right
            return s
        
        return longestNiceSubstringRecursive(s)