class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"  # Handle the case when numerator is 0

        result = ""  # Initialize the result string

        # Handle the sign of the result
        if numerator * denominator < 0:
            result += "-"
            numerator = abs(numerator)
            denominator = abs(denominator)

        # Append the integer part to the result string
        result += str(numerator // denominator)

        remainder = numerator % denominator  # Initialize the remainder
        if remainder == 0:
            return result  # If there is no fractional part, return the result
        
        result += "."  # Append '.' to indicate the start of the fractional part

        # Dictionary to store remainders and their positions
        remainders = {}

        # Perform long division
        while remainder != 0:
            # If the remainder repeats, insert '(' and ')' in the result string
            if remainder in remainders:
                result = result[:remainders[remainder]] + "(" + result[remainders[remainder]:] + ")"
                break  # Break the loop as repeating pattern detected
            remainders[remainder] = len(result)  # Store the position of the remainder
            remainder *= 10  # Bring down the next digit
            result += str(remainder // denominator)  # Append the quotient to the result
            remainder %= denominator  # Update the remainder
        
        return result


