class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        def fun(n):
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            return fun(n/3)
        return fun(n)