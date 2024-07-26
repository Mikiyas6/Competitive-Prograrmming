class Solution:
    def reorganizeString(self, s: str) -> str:
    
        freq = Counter(s)
        
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        prev_char = None
        prev_freq = 0
        result = []
        
        while max_heap:
    
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            if prev_char and prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_char = char
            prev_freq = freq + 1
        
        if len(result) != len(s):
            return ""
        else:
            return "".join(result)