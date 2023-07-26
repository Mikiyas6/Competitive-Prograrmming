# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        if not isBadVersion(n-1):
            return n
        while end >= start:
            middle = start + (end-start)//2
            if isBadVersion(middle):
                if not isBadVersion(middle-1):
                    return middle
                end = middle - 1
            else:
                if isBadVersion(middle+1):
                    return middle+1
                start = middle + 1
