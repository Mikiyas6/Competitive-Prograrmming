class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1 or n == 2:

            return True
        
        if n == 0 or n % 2 != 0:

            return False
        
        n = n // 2

        return self.isPowerOfTwo(n)

