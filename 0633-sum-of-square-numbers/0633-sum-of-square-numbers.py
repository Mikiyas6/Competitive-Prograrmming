class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        i = 0
        j = int(sqrt(c))

        while i <= j:

            square = i**2 + j**2

            if square < c:

                i += 1
            
            elif square > c:

                j -= 1

            else:

                return True

        return False