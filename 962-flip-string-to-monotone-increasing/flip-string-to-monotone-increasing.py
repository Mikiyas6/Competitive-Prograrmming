class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        ones = flips = 0

        for digit in s:
            if digit == '1':
                ones += 1
            else:
                flips += 1
            
            flips = min(flips, ones)

        return flips