class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        max_seen = 0  # Initialize the maximum element seen so far
        chunks = 0  # Initialize the number of chunks

        for i, num in enumerate(arr):
            max_seen = max(max_seen, num)  # Update the maximum element seen so far
            if max_seen == i:  # If the maximum element seen so far equals the index
                chunks += 1  # Increment the number of chunks

        return chunks
