class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 0):
            return False
        elif (n == 1):
            return True
        if (n %4 != 0):
            return False
        elif( n == 4):
            return True
        else:
            return self.isPowerOfFour(n/4)
