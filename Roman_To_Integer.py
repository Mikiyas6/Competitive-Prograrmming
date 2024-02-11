class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a mapping of Roman numeral symbols to their corresponding integer values
        mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }
        
        # Initialize the total value
        total = 0
        
        # Iterate through the Roman numeral string
        i = 0
        while i < len(s):
            # Check for subtraction cases
            if i + 1 < len(s) and s[i:i+2] in mapping:
                total += mapping[s[i:i+2]]
                i += 2  # Move the iterator two steps forward
            else:
                total += mapping[s[i]]
                i += 1  # Move the iterator one step forward
        
        # Return the total value
        return total
