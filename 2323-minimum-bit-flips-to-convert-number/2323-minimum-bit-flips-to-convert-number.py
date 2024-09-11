class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR to find differing bits between start and goal
        xor_result = start ^ goal
        count = 0
        
        # Count the number of 1's in the XOR result
        while xor_result > 0:
            count += xor_result & 1  # Check if the least significant bit is 1
            xor_result >>= 1         # Right shift to check the next bit
        
        return count