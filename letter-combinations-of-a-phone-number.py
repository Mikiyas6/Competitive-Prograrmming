class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        # Create a mapping of digits to letters
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Initialize the result list
        result = []
        
        # Helper function to backtrack and generate combinations
        def backtrack(combination, next_digits):
            # If there are no more digits to check, add the combination to the result
            if not next_digits:
                result.append(combination)
            else:
                # Iterate through the letters corresponding to the next digit
                for letter in mapping[next_digits[0]]:
                    # Backtrack with the current combination plus the current letter
                    backtrack(combination + letter, next_digits[1:])
        
        # Start the backtracking process with an empty combination and the input digits
        backtrack('', digits)
        
        return result
