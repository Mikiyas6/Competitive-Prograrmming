class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:

            return 1
        
        s = 0
        e = x//2

        def floor(s,e,target):
    
            if s > e:
                
                return e
            
            mid = (s+(e-s)//2)

            square = mid**2
            
            if square == target:
                
                return mid
            
            if target < square:
                
                e = mid-1
            
            else:
                
                s = mid+1
            
            return floor(s,e,target)
        
        return floor(s,e,x)
        




        