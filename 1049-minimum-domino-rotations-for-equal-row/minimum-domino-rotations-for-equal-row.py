class Solution:
    def minDominoRotations(self, a: List[int], b: List[int]) -> int:
        return next((len(a)-max(a.count(v),b.count(v)) for v in (a[0],b[0]) 
            if all(v in p for p in zip(a,b))),-1)