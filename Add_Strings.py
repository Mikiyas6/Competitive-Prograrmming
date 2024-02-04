class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        result = []
        carry = 0

        # Make the lengths of num1 and num2 equal by prepending zeros
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))

        for i in range(len(num1) - 1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            result.append(str(digit_sum % 10))
            carry = digit_sum // 10

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])
