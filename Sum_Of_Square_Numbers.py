class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        i = 0
        j = int(c**0.5) 

        while i <= j:

            product =  i**2 + j**2

            if product == c:
                return True
            elif product > c:
                j -= 1
            else:
                i += 1

        return False
