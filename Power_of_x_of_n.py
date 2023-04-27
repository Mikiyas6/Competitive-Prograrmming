class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if (n == 0):
            return 1
        elif (n == 1):
            return x
        elif (n > 999 or n < -999):
            return x ** n
        elif n > 1:
            return x * self.myPow(x,n-1)
        else:
            return self.myPow(x, n+1)/x
