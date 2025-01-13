class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def findK(k):
            time = 0
            for pile in piles:
                if pile <= k:
                    time += 1
                else:
                    time += math.ceil(pile/k)
            return time
        
        start = 1
        end = max(piles)
        while start <= end:
            mid = start + (end-start)//2
            result = findK(mid)
            if result > h:
                start = mid+1
            else:
                end = mid-1
        return start
        
            