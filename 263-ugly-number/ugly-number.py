class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        array = [2,3,5]

        for value in array:

            while n % value == 0:

                n = n // value
        
        if n == 1:

            return True