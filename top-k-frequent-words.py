class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # Step 1: Count the frequency of each word
        freq_counter = Counter(words)
        
        # Step 2: Push word-frequency pairs into a max heap
        max_heap = [(-freq, word) for word, freq in freq_counter.items()]
        heapq.heapify(max_heap)
        
        # Step 3: Pop the top k elements from the max heap
        result = []
        for _ in range(k):
            freq, word = heapq.heappop(max_heap)
            result.append(word)
        
        # Step 4: Sort the result by frequency (descending) and then lexicographically (ascending)
        result.sort(key=lambda x: (-freq_counter[x], x))
        
        return result
        
            
