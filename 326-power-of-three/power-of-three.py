class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0:

            return False
        
        if n == 1:

            return True
        
        if n % 3 != 0:

            return False
        
        return True and self.isPowerOfThree(n//3)