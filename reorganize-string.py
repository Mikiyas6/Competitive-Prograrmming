class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)
        rearranged = []

        while counter:
            prev_char = rearranged[-1] if rearranged else None
            max_freq_char = None

            for char, freq in counter.items():
                if char != prev_char and (max_freq_char is None or freq > counter[max_freq_char]):
                    max_freq_char = char

            if max_freq_char is None:
                return ""

            rearranged.append(max_freq_char)
            counter[max_freq_char] -= 1
            if counter[max_freq_char] == 0:
                del counter[max_freq_char]

        return ''.join(rearranged)
