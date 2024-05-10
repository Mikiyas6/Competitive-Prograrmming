class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat_all(piles, k, hours):
            hours_count = 0
            for pile in piles:
                hours_count += math.ceil(pile/k)
            
            if hours_count > hours:
                return False
            return True

        s, e = 1, max(piles)
        k = e
        while s <= e:
            mid = s + (e - s) // 2
            if can_eat_all(piles, mid, h):
                k = min(k,mid)
                e = mid-1
            else:
                s = mid+1
        return k