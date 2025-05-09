class Solution:
    def reorganizeString(self, s: str) -> str:
        
        hashmap = Counter(s)
        max_heap = [(-freq, char) for char, freq in hashmap.items()]
        heapify(max_heap)

        prev_char = None
        prev_freq = 0
        result = []

        while max_heap:
            freq, char = heappop(max_heap)
            result.append(char)

            if prev_char and prev_freq < 0:
                heappush(max_heap,(prev_freq,prev_char))
            
            prev_char = char
            prev_freq = freq + 1

        if len(result) != len(s):
            return ""
        return "".join(result)