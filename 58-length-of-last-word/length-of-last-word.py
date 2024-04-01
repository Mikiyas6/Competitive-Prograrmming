class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        words = list(map(str,s.split()))

        return len(words[-1])