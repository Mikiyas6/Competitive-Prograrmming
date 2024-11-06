class Solution:
    def findNthDigit(self, n: int) -> int:
        x,y,q=1,1,10
        while q<n:
            x,y=q,y+1,
            q=x+9*y*(10**(y-1))
        return int(str((10**(y-1))+((n-x)//(y)))[(n-x)%(y)])