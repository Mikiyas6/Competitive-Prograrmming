class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        min_heap = [] 
        min_heap.append(1) 
        vis = {1} 
        curr = 0

        for i in range(n):
            curr = heapq.heappop(min_heap)
            for prime in primes:
                new = curr * prime
                if new not in vis:
                    vis.add(new)
                    heapq.heappush(min_heap, new)
        
        return curr