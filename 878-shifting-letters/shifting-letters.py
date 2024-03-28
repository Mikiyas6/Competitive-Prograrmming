class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        n = len(shifts)

        offset = ord("a")

        cumulative = 0

        right_prefix_sum = [0] * n

        for i in range(n-1,-1,-1):

            cumulative += shifts[i]

            right_prefix_sum[i] = cumulative
        
        lists = []

        for index,character in enumerate(s):

            shift = right_prefix_sum[index]

            value = ord(character) - offset

            value = (value + shift) % 26

            value += offset
        
            lists.append(chr(value))
        
        return "".join(lists)






        