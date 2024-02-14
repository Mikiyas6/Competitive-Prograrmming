class Solution:
    def originalDigits(self, s: str) -> str:
        
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        digit_count = {}
        digit_count[0] = char_count.get('z', 0)
        digit_count[2] = char_count.get('w', 0)
        digit_count[4] = char_count.get('u', 0)
        digit_count[6] = char_count.get('x', 0)
        digit_count[8] = char_count.get('g', 0)
        digit_count[1] = char_count.get('o', 0) - digit_count[0] - digit_count[2] - digit_count[4]
        digit_count[3] = char_count.get('h', 0) - digit_count[8]
        digit_count[5] = char_count.get('f', 0) - digit_count[4]
        digit_count[7] = char_count.get('s', 0) - digit_count[6]
        digit_count[9] = char_count.get('i', 0) - digit_count[5] - digit_count[6] - digit_count[8]

        result = ""
        for i in range(10):
            result += str(i) * digit_count[i]

        return result