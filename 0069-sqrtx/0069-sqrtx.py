class Solution:
    def mySqrt(self, x: int) -> int:
        
        def floor(start,end):
            if start > end:
                return end
            mid = start + (end-start)//2
            square = mid*mid
            if square == x:
                return mid
            if x < square:
                end = mid-1
            else:
                start = mid+1
            return floor(start,end)
        
        return floor(0,x)