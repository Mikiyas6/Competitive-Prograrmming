class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findHours(piles,k):
            count = 0
            for pile in piles:
                if pile <= k:
                    count += 1
                else:
                    count += math.ceil(pile/k)
            return count

        def findK(start,end,piles,h):
            if start > end:
                return start
            k = start + (end-start)//2
            hours = findHours(piles,k)
            if hours <= h:
                end = k-1
            else:
                start = k+1
            return findK(start,end,piles,h)

        start = 1
        end = max(piles)
        return findK(start,end,piles,h)
        