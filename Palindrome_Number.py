class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        
        return True if x == x[::-1] else False
