class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Create a frequency map for characters in the string
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
        
        # Sort characters based on their frequencies in decreasing order
        sorted_chars = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)
        
        # Construct the sorted string based on the sorted characters and their frequencies
        sorted_string = ''.join(char * freq_map[char] for char in sorted_chars)
        
        return sorted_string
