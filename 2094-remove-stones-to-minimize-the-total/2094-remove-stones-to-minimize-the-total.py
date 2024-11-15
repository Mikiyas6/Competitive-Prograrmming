class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        maxHeap = [-1*pile for pile in piles]
        heapify(maxHeap)

        for _ in range(k):
            if maxHeap:
                value = heappop(maxHeap)
                modified = math.ceil((-1*value)/2)
                heappush(maxHeap,-1*modified)
        
        return -1*sum(maxHeap)