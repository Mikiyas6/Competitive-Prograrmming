class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c**0.5)
        if j == 0:
            j = 1
        while i <= j:
            if i**2 + j**2 > c:
                j -= 1
            elif i**2 + j**2 < c:
                i += 1
            else:
                return True
        return False
