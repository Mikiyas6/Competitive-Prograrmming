class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res = 9
        j = 9
        for i in range(n-1):
            res *= j
            j -= 1
        return res + self.countNumbersWithUniqueDigits(n-1)