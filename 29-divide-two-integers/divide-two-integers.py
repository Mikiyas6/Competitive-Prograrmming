class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # Handle edge cases where divisor is 0 or dividend is the minimum value and divisor is -1
        if divisor == 0 or (dividend == -2**31 and divisor == -1):
            return 2**31 - 1
        
        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Convert both dividend and divisor to positive to simplify calculation
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        # Repeat until dividend is greater than or equal to divisor
        while dividend >= divisor:
            # Initialize the value of the current quotient bit
            current_quotient = 1
            # Initialize the value of the current divisor (will be doubled in each iteration)
            current_divisor = divisor
            
            # Double the current divisor until it becomes greater than the remaining dividend
            while current_divisor <= (dividend >> 1):
                current_divisor <<= 1
                current_quotient <<= 1
            
            # Subtract the current divisor from the remaining dividend
            dividend -= current_divisor
            # Add the current quotient bit to the result
            quotient += current_quotient

        return sign * quotient