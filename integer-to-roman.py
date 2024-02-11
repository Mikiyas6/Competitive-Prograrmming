class Solution:
    def intToRoman(self, num: int) -> str:
    
        mapping = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 
            100: "C", 90: "XC", 50: "L", 40: "XL", 
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
        
        # Initialize an empty string to store the Roman numeral
        roman = ""
        
        # Iterate through the mapping from largest to smallest value
        for value, symbol in sorted(mapping.items(), reverse=True):
            # Check if the given integer is greater than or equal to the current value
            while num >= value:
                # Subtract the current value from the integer
                num -= value
                # Append the corresponding Roman numeral symbol to the result string
                roman += symbol
        
        # Return the resulting Roman numeral string
        return roman
