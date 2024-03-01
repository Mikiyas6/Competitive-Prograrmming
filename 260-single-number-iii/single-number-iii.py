class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        # XOR all elements to get XOR of the two single numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # Find any bit that is set to 1 in xor_result
        # We can use the rightmost set bit for simplicity
        rightmost_set_bit = 1
        while (rightmost_set_bit & xor_result) == 0:
            rightmost_set_bit <<= 1

        # Separate the two single numbers based on the bit
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]