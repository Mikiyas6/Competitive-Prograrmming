class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        
        prefix_sum = [0] * (n+1)

        for start,end,direction in shifts:

            if direction == 0:

                direction = -1
            
            prefix_sum[start] += direction

            prefix_sum[end+1] -= direction
        
        cumulative = 0

        for index, value in enumerate(prefix_sum):

            cumulative += value

            prefix_sum[index] = cumulative
        
        offset = ord("a")

        string = ""
        
        prefix_sum = prefix_sum[:n]

        for index, shift in enumerate(prefix_sum):

            converted = ord(s[index])

            calibrated = converted - offset

            total_shift = (calibrated + shift) % 26

            new_char = chr(total_shift+offset)

            string += new_char
        
        return string