class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        A,B=-1,-1 
        numberOfGroups=0
        for a,b in ranges:
            if B<a:
                numberOfGroups+=1
                A,B=a,b
            else:
                B=max(B,b)
        return pow(2,numberOfGroups,10**9+7)      