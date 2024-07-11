class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap) 
            largest -= largest // 2 
            heapq.heappush(max_heap, -largest)  
        
        return -sum(max_heap)