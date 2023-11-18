class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        prefix_sum = [0] * (len(s)+1)

        for l,r,value in shifts:

            if value == 0:
                value = -1
            else:
                value = 1

            prefix_sum[l] += value
            prefix_sum[r+1] -= value
        
        cumulative = 0

        for index,value in enumerate(prefix_sum):

            cumulative += value
            prefix_sum[index] = cumulative
        
        prefix_sum = prefix_sum[:len(s)]

        string = ""
        offset = ord("a")

        for index,value in enumerate(s):

            movement = (ord(value) - offset) + prefix_sum[index]
            
            if prefix_sum[index] > 0:

                string += chr(((movement) % 26) + offset)
            
            elif prefix_sum[index] < 0:

                string += chr(((movement + 26) % 26) + offset)

            else:

                string += value
            
        return string



