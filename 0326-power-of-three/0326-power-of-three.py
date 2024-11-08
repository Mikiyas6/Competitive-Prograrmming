class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def fun(n):
            if n < 9:
                if n == 1 or n == 3:
                    return True
                return False
            return fun(n/9)
        return fun(n)