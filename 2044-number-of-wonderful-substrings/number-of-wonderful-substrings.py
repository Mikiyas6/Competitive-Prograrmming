class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        result = 0
        mask = 0
        count = {0: 1}  # Initialize count with 0 having count 1
        for char in word:
            char_mask = 1 << (ord(char) - ord('a'))
            mask ^= char_mask  # Toggle the bit corresponding to the current character
            result += count.get(mask, 0)  # Add the count of the current mask to the result
            for i in range(10):  # Iterate over all possible masks
                result += count.get(mask ^ (1 << i), 0)  # Add the count of complementary mask to the result
            count[mask] = count.get(mask, 0) + 1  # Update the count of the current mask
        return result