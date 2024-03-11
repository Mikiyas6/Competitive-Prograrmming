class Solution:
    def nextGreaterElement(self, n: int) -> int:

        digits = list(str(n))
        length = len(digits)
        pivot = -1
        for i in range(length - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i
                break

        if pivot == -1:
            return -1  
        for i in range(length - 1, pivot, -1):
            if digits[i] > digits[pivot]:
                swap_digit = i
                break
        digits[pivot], digits[swap_digit] = digits[swap_digit], digits[pivot]
        digits[pivot + 1:] = sorted(digits[pivot + 1:])
        result = int(''.join(digits))
        return result if result < 2**31 else -1