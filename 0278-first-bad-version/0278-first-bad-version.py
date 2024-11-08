# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        start = 0
        end = n

        def fun(start,end):
            if start > end:
                return 0
            mid = start + (end-start)//2
            if isBadVersion(mid):
                if mid-1 >= 0 and not isBadVersion(mid-1):
                    return mid
                else:
                    end = mid-1
            else:
                start = mid+1
            
            return fun(start,end)
        
        return fun(start,end)