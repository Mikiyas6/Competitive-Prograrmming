class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
    
        hashmap = Counter(words)

        max_heap = [(-freq, word) for word, freq in hashmap.items()]
        heapq.heapify(max_heap)

        result = []
        for _ in range(k):
            freq, word = heapq.heappop(max_heap)
            result.append(word)

        result.sort(key=lambda word: (-hashmap[word], word))
        
        return result
        
            