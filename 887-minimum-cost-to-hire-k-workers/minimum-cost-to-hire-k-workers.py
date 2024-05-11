class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        heap = []
        sumq = 0
        ans = float('inf')
        for r, q in workers:
            heapq.heappush(heap, -q)
            sumq += q
            if len(heap) > k:
                sumq += heapq.heappop(heap)
            if len(heap) == k:
                ans = min(ans, sumq * r)
        return ans