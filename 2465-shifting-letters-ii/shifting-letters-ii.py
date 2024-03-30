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

        # To shift 

              # idx = (idx + shift_amount) % 26

        # if shift_amount is negative and makes (idx + shift_amount) negative, then you will have to add the size to it 

              # idx = (idx + shift_amount + 26) % 26

        for index, shift in enumerate(prefix_sum):

            converted = ord(s[index])

            calibrated = converted - offset

            shifted = calibrated + shift

            if shifted < 0:

                shifted += 26

            total_shift = shifted % 26

            new_char = chr(total_shift+offset)

            string += new_char
        
        return string