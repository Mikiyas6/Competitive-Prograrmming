class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shift = 0
        result = []
        for i in range(len(shifts) - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            new_char = chr((ord(s[i]) - ord('a') + total_shift) % 26 + ord('a'))
            result.insert(0, new_char)
        return ''.join(result)