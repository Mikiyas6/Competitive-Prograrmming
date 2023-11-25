class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefix_sum = [0] * (len(s) + 1)

        for start,end,direction in shifts:

            direction = 1 if direction == 1 else -1

            prefix_sum[start] += direction
            prefix_sum[end+1] -= direction
        
        cumulative = 0

        for index,value in enumerate(prefix_sum):

            cumulative += value
            prefix_sum[index] = cumulative
        
        preifx_sum = prefix_sum[:len(s)]

        string = ""
        offset = ord("a")

        for index,value in enumerate(s):

            shift_amount = prefix_sum[index]
            letter = ord(value) - offset

            if shift_amount >= 0:

                string += chr(((letter + shift_amount) % 26) + offset)
            
            elif shift_amount < 0:

                string += chr(((letter + shift_amount + 26) % 26) + offset)
        
        return string
            
