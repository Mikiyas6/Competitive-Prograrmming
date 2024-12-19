class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen = 0  
        chunks = 0  
        for i, num in enumerate(arr):
            max_seen = max(max_seen, num)  
            if max_seen == i:  
                chunks += 1  
        return chunks