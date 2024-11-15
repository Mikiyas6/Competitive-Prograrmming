class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-1*value for value in nums]
        heapify(maxHeap)
        result = 0
        while k != 0:
            result = heappop(maxHeap)
            k -= 1
        return -1*result